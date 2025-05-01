# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str
    FROM_EMAIL: str

    RABBITMQ_URL: str
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_file = ".env"

settings = Settings()