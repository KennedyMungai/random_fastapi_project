"""The model definiition file"""
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class Post(Base):
    """The template for the Post table in the database"""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published = Column(Boolean, default=True, nullable=False)
