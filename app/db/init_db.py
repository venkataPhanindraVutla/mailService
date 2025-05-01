# File: app/db/init_db.py
from app.db.session import engine
from app.db.base_class import Base
from app.db.models import email_log

def init_db():
    Base.metadata.create_all(bind=engine)