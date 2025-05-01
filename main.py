"""
Main application file for the Mail Service.
Sets up the FastAPI application and includes the mail router.
"""
from fastapi import FastAPI
from app.routes import mail
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include the mail router with a prefix and tags
app.include_router(mail.router, prefix="/mail", tags=["Mail"])