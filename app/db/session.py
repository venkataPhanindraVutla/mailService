"""
Database session configuration and dependency.
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings

# Create the asynchronous SQLAlchemy engine
# Use echo=True for debugging SQL queries (optional)
engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False)

# Create a configured "AsyncSession" class
AsyncSessionLocal = async_sessionmaker(
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

async def get_db() -> AsyncSession:
    """
    Dependency that provides an asynchronous database session.

    Yields:
        AsyncSession: An asynchronous SQLAlchemy session object.
    """
    async with AsyncSessionLocal() as db:
        yield db
