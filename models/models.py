"""The model definition file"""
from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String

from db.database import Base


class Post(Base):
    """The template for the Post table in the database"""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published = Column(Boolean, default=1, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow())


class User(Base):
    """The model for the db user tab;e

    Args:
        Base (Class): A declarative base for the database and such
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow())
