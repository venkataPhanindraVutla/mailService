"""
Base class for SQLAlchemy models.
"""
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer

@as_declarative()
class Base:
    """
    Base class for SQLAlchemy models, providing a default table name
    and a primary key 'id'.
    """
    id = Column(Integer, primary_key=True, index=True)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generates the table name based on the class name.
        """
        return cls.__name__.lower()

    def __repr__(self) -> str:
        """
        Provides a string representation of the model instance.
        """
        return f"<{self.__class__.__name__} {self.id}>"