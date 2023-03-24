"""The main file for the project"""
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from db.database import engine, get_db
from models import models
from models.models import Post

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: Returns a message to show successful execution
    """
    return {"message": "The api works"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(_post: Post, _db: Session = Depends(get_db)):
    pass
