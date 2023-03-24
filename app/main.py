"""The main file for the project"""
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from db.database import engine, get_db
from models import models

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
async def test_posts(_db: Session = Depends(get_db)) -> dict:
    """A dummy endpoint to check for connection with the database

    Args:
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A message to show successful execution
    """
    _retrieved_posts = _db.query(models.Post).all()

    return {"Message": _retrieved_posts}
