# app/db/models/email_log.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)
    to_email = Column(String(255), nullable=False)
    subject = Column(String(255))
    body = Column(Text)
    status = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
