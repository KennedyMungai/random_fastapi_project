"""Created the file containing the Posts Schemas"""
from pydantic import BaseModel


class PostBase(BaseModel):
    """The base class representing the Post daya

    Args:
        BaseModel (Class): The parent class
    """
    title: str
    content: str
    published: bool


class PostCreate(PostBase):
    """The template for teh Create Post data

    Args:
        BaseModel (Class): The parent class for the CreatePost class
    """
