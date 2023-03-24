"""The main file for the project"""
from fastapi import Depends, FastAPI

from db.database import engine, get_db
from models import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: Returns a message to show successful execution
    """
    return {"message": "The api works"}


@app.get("/sqlalchemy")
async def test_posts(_db: Session = Depends(get_db)):
    pass
