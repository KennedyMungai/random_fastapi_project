"""Created the file containing the Posts Schemas"""
from datetime import datetime

from pydantic import BaseModel

from .user_schemas import UserResponse


class PostBase(BaseModel):
    """The base class representing the Post data

    Args:
        BaseModel (Class): The parent class
    """
    id: int
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    """The template for teh Create Post data

    Args:
        BaseModel (Class): The parent class for the CreatePost class
    """


class PostResponse(PostBase):
    """The template for the Post response data

    Args:
        BaseModel (Class): The parent class
    """
    created_at: datetime
    owner: UserResponse

    class Config:
        """The configuration for the PostResponse class"""
        orm_mode = True
