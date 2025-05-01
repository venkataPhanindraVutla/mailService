# app/schemas/mail.py
from pydantic import BaseModel, EmailStr

class MailRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str
