"""The main file for the project"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from db.database import SessionLocal, engine
from models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    _db = SessionLocal()

    try:
        yield _db
    finally:
        _db.close()


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
