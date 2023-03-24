"""The main file for the project"""
from fastapi import Depends, FastAPI, HTTPException, status
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
    _new_post = Post(**_post.dict())

    _db.add(_new_post)
    _db.commit()
    _db.refresh(_new_post)

    return {"Message": _new_post}


@app.get("/posts/{_id}")
async def retrieve_one_post(_id: int, _db: Session = Depends(get_db)) -> dict:
    """The endpoint to retrieve one post by its Id

    Args:
        _id (int): The id of the post
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the retrieved post
    """
    _post = _db.query(Post).filter(Post.id == _id).first()

    if not _post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"A post with id {_id} was not found"
        )

    return {"Post": _post}


@app.get("/posts", status_code=status.HTTP_200_OK)
async def retrieve_all_posts(_db: Session = Depends(get_db)):
    """An endpoint to retrieve all the posts in the database

    Args:
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List: A list of all posts
    """
    _all_posts = _db.query(Post).all()
    return _all_posts


@app.delete("/posts/{_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(_id: int, _db: Session = Depends(get_db)):
    """The delet Post endpoint

    Args:
        _id (int): The id of the Post
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: A 404 is returned if Post Id is not found
    """
    _post = _db.query(Post).filter(Post.id == _id).first()

    if not _post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The post with id of {_id} was not found"
        )

    _db.delete(_post)
    _db.commit()
