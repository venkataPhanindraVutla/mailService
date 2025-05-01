# app/services/mail.py
from app.core.mailer import Mailer
from app.db.session import get_db
from app.db.models.email_log import EmailLog
from app.utils.exceptions import handle_exceptions
from sqlalchemy.ext.asyncio import AsyncSession

class MailService:
    def __init__(self, mailer: Mailer):
        self.mailer = mailer

    @handle_exceptions
    async def send_and_log(self, to_email: str, subject: str, body: str, db: AsyncSession):
        await self.mailer.send_email(to_email, subject, body)
        log = EmailLog(to_email=to_email, subject=subject, body=body, status="sent")
        db.add(log)
        await db.commit()