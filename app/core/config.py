"""
Configuration settings for the mail service.
Settings are loaded from environment variables or a .env file.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings class.

    Attributes:
        PROJECT_NAME (str): The name of the project.
        SMTP_HOST (str): The SMTP server host.
        SMTP_PORT (int): The SMTP server port.
        SMTP_USER (str): The SMTP username.
        SMTP_PASS (str): The SMTP password.
        FROM_EMAIL (str): The sender's email address.
        RABBITMQ_URL (str): The URL for the RabbitMQ server.
        SQLALCHEMY_DATABASE_URI (str): The database connection URI.
    """
    PROJECT_NAME: str = "Mail Service"
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str
    FROM_EMAIL: str

    RABBITMQ_URL: str
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = True

settings = Settings()