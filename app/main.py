"""The main file for the project"""
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from db.database import engine, get_db
from models import models
from models.models import Post
from schemas.PostSchemas import CreatePost

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
async def create_post(_post: CreatePost, _db: Session = Depends(get_db)) -> dict:
    """The create post endpoint

    Args:
        _post (CreatePost): The new post
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the created post
    """
    _new_post = Post(_post)

    _db.add(_new_post)
    _db.commit()
    _db.refresh(_new_post)

    return {"Message": _new_post}


@app.get("/posts", status_code=status.HTTP_200_OK)
async def retrieve_all_posts(_db: Session = Depends(get_db)):
    _all_posts = _db(Post).all()
    return _all_posts
