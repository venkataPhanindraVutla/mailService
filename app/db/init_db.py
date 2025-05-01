"""
Initializes the database by creating all tables defined in the models.
"""
from app.db.session import engine
from app.db.base_class import Base
# Import all models here to ensure they are registered with SQLAlchemy Base
from app.db.models import email_log

def init_db():
    """
    Creates all database tables based on the SQLAlchemy models.
    """
    Base.metadata.create_all(bind=engine)