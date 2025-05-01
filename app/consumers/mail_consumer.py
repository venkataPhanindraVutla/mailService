# app/consumers/mail_consumer.py
import aio_pika
import json
from app.core.config import settings
from app.core.mailer import Mailer
from app.services.mail import MailService
from app.db.session import get_db

async def consume():
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue("mail_queue", durable=True)

    mailer = Mailer()
    service = MailService(mailer)

    async with get_db() as db:
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    data = json.loads(message.body.decode())
                    await service.send_and_log(
                        to_email=data["to_email"],
                        subject=data["subject"],
                        body=data["body"],
                        db=db
                    )