import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Settings:
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

    def __init__(self):
        """
        Initializes the settings by loading values from environment variables.
        """
        self.SMTP_HOST = os.environ.get("SMTP_HOST")
        self.SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))  # Default port if not set
        self.SMTP_USER = os.environ.get("SMTP_USER")
        self.SMTP_PASS = os.environ.get("SMTP_PASS")
        self.FROM_EMAIL = os.environ.get("FROM_EMAIL")
        self.RABBITMQ_URL = os.environ.get("RABBITMQ_URL")
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

settings = Settings()
