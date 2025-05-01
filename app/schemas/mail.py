"""
Pydantic models for mail service request and response schemas.
"""
from pydantic import BaseModel, EmailStr

class MailRequest(BaseModel):
    """
    Schema for incoming mail sending requests.

    Attributes:
        to_email (EmailStr): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    """
    to_email: EmailStr
    subject: str
    body: str
