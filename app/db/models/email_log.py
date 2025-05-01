"""
SQLAlchemy model for logging sent emails.
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class EmailLog(Base):
    """
    Represents a log entry for a sent email.

    Attributes:
        id (int): Primary key, auto-incrementing.
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.
        status (str): The status of the email sending (e.g., 'sent', 'failed').
        created_at (datetime): Timestamp when the log entry was created.
    """
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)
    to_email = Column(String(255), nullable=False)
    subject = Column(String(255))
    body = Column(Text)
    status = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
