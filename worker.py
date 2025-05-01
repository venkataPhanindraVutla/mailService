"""
Worker file to run the RabbitMQ mail consumer.
"""
import asyncio
from app.consumers.mail_consumer import consume

if __name__ == "__main__":
    """
    Runs the asynchronous mail consumer.
    """
    asyncio.run(consume())