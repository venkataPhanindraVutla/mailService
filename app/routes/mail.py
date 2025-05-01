"""
API routes for the mail service.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.mail import MailRequest
from app.db.session import get_db, AsyncSessionLocal
from app.db.models.email_log import EmailLog
from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
import aio_pika
import json

router = APIRouter()

async def publish_mail_task(to_email: str, subject: str, body: str, log_id: int):
    """
    Publishes a mail sending task to the RabbitMQ queue.
    Includes the log_id to update the status later.
    """
    try:
        connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
        async with connection:
            channel = await connection.channel()
            await channel.declare_queue("mail_queue", durable=True)

            message_body = json.dumps({
                "to_email": to_email,
                "subject": subject,
                "body": body,
                "log_id": log_id
            }).encode()

            await channel.default_exchange.publish(
                aio_pika.Message(body=message_body),
                routing_key="mail_queue"
            )
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error publishing message to RabbitMQ: {e}")
        # In case of failure to publish, update the log status to indicate failure
        async with AsyncSessionLocal() as db:
            result = await db.execute(select(EmailLog).where(EmailLog.id == log_id))
            email_log = result.scalars().first()
            if email_log:
                email_log.status = f"publish_failed: {e}"
                await db.commit()
        raise HTTPException(status_code=500, detail="Failed to queue email task")


@router.post("/send")
async def send_mail(request: MailRequest, db: AsyncSession = Depends(get_db)):
    """
    Creates an email log entry and queues an email sending task to RabbitMQ.

    Args:
        request (MailRequest): The request body containing email details.
        db (AsyncSession): Database session dependency.

    Returns:
        dict: A confirmation message indicating the task has been queued.
    """
    # Create a log entry with 'queued' status
    log = EmailLog(to_email=request.to_email, subject=request.subject, body=request.body, status="queued")
    db.add(log)
    await db.commit()
    await db.refresh(log) # Refresh to get the generated log_id

    # Publish the task to RabbitMQ with the log_id
    await publish_mail_task(request.to_email, request.subject, request.body, log.id)

    return {"message": "Email task queued successfully", "log_id": log.id}