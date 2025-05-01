"""
Service layer for handling mail sending and logging.
"""
from app.core.mailer import Mailer
from app.db.models.email_log import EmailLog
from app.utils.exceptions import handle_exceptions
from sqlalchemy.ext.asyncio import AsyncSession

class MailService:
    """
    Provides methods for sending emails and logging the transactions.
    """
    def __init__(self, mailer: Mailer):
        """
        Initializes the MailService with a Mailer instance.

        Args:
            mailer (Mailer): The mailer instance to use for sending emails.
        """
        self.mailer = mailer

    @handle_exceptions
    async def send_and_log(self, to_email: str, subject: str, body: str, db: AsyncSession):
        """
        Sends an email and logs the transaction to the database.

        Args:
            to_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body content of the email.
            db (AsyncSession): The database session.
        """
        # The actual email sending is now handled by the RabbitMQ consumer.
        # This method is primarily for logging the attempt to send.
        log = EmailLog(to_email=to_email, subject=subject, body=body, status="queued")
        db.add(log)
        await db.commit()
        # Note: The status will be updated to 'sent' or 'failed' by the consumer