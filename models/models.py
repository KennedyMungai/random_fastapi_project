"""The model definiition file"""
from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String

from db.database import Base


class Post(Base):
    """The template for the Post table in the database"""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow())
