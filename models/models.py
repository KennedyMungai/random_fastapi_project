"""The model definition file"""
from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Post(Base):
    """The template for the Post table in the database"""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published = Column(Boolean, default=1, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow())
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")


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


class Votes(Base):
    """Created the model for the Votes table

    Args:
        Base (A function): Does something
    """
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"),
                     primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"),
                     primary_key=True, nullable=False)
