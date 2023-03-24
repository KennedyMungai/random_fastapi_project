"""Created the file containing the Posts Schemas"""
from pydantic import BaseModel


class CreatePost(BaseModel):
    """The template for teh Create Post data

    Args:
        BaseModel (Class): The parent class for the CreatePost class
    """
    title: str
    content: str
    published: bool
