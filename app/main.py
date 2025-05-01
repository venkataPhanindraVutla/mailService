# app/main.py
from fastapi import FastAPI
from app.routes import mail
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(mail.router, prefix="/mail", tags=["Mail"])