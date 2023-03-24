"""The main file for the project"""
from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Post(BaseModel):
    """The post model

    Args:
        BaseModel (Class): The parent class
    """
    title: str
    content: str
    published: Optional[bool] = True


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: Returns a message to show successful execution
    """
    return {"message": "The api works"}


@app.post("/createposts")
async def create_posts(payload: Post) -> dict:
    """A dummy post creator endpoint

    Returns:
        dict: A message to show successful code execution
    """
    return {"new post": payload}
