# worker.py
import asyncio
from app.consumers.mail_consumer import consume

if __name__ == "__main__":
    asyncio.run(consume())