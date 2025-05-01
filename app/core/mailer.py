"""
Mailer class for sending emails using SMTP.
"""
import aiosmtplib
from email.message import EmailMessage
from app.core.config import settings

class Mailer:
    """
    Handles sending emails via SMTP.
    """
    def __init__(self):
        """
        Initializes the Mailer with SMTP settings from configuration.
        """
        self.host = settings.SMTP_HOST
        self.port = settings.SMTP_PORT
        self.user = settings.SMTP_USER
        self.password = settings.SMTP_PASS
        self.from_email = settings.FROM_EMAIL

    async def send_email(self, to_email: str, subject: str, body: str):
        """
        Sends an email to the specified recipient.

        Args:
            to_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body content of the email.
        """
        message = EmailMessage()
        message["From"] = self.from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content(body)

        await aiosmtplib.send(
            message,
            hostname=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            start_tls=True
        )
