"""
RabbitMQ consumer for processing mail sending tasks.
"""
import aio_pika
import json
from app.core.config import settings
from app.core.mailer import Mailer
from app.db.session import AsyncSessionLocal
from app.db.models.email_log import EmailLog
from app.core.mailer import Mailer
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def consume():
    """
    Connects to RabbitMQ, declares the mail queue, and consumes messages.
    For each message, it sends the email using the Mailer and updates the
    email log status in the database.
    """
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue("mail_queue", durable=True)

    mailer = Mailer()

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                print(f"Received message: {message.body.decode()}")
                data = json.loads(message.body.decode())
                to_email = data.get("to_email")
                subject = data.get("subject")
                body = data.get("body")
                log_id = data.get("log_id") # Assuming log_id is passed in the message

                if not all([to_email, subject, body, log_id]):
                    print("Invalid message format, skipping.")
                    continue

                async with AsyncSessionLocal() as db:
                    try:
                        # Send the email
                        await mailer.send_email(to_email, subject, body)

                        # Update the log status to 'sent'
                        result = await db.execute(select(EmailLog).where(EmailLog.id == log_id))
                        email_log = result.scalars().first()
                        if email_log:
                            email_log.status = "sent"
                            await db.commit()
                            print(f"Email sent and log updated for ID: {log_id}")
                        else:
                            print(f"Email log with ID {log_id} not found.")

                    except Exception as e:
                        # Update the log status to 'failed' on error
                        print(f"Error sending email for ID {log_id}: {e}")
                        async with AsyncSessionLocal() as error_db:
                             result = await error_db.execute(select(EmailLog).where(EmailLog.id == log_id))
                             email_log = result.scalars().first()
                             if email_log:
                                email_log.status = f"failed: {e}"
                                await error_db.commit()
                             else:
                                print(f"Email log with ID {log_id} not found during error handling.")