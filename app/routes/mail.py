# app/api/routes/mail.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.mail import MailRequest
from app.services.mail import MailService
from app.db.session import get_db
from app.core.mailer import Mailer

router = APIRouter()

@router.post("/send")
async def send_mail(request: MailRequest, db: AsyncSession = Depends(get_db)):
    mailer = Mailer()
    service = MailService(mailer)
    await service.send_and_log(request.to_email, request.subject, request.body, db)
    return {"message": "Email sent successfully"}