"""
Main application file for the Mail Service.
Sets up the FastAPI application and includes the mail router.
"""
import uvicorn
from fastapi import FastAPI
from app.routes import mail
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include the mail router with a prefix and tags
app.include_router(mail.router, prefix="/mail", tags=["Mail"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)