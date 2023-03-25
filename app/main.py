"""The main file for the project"""
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from db.database import engine, get_db
from models import models
from models.models import Post, User
from schemas.PostSchemas import PostCreate, PostResponse
from schemas.UserSchemas import UserRequest, UserResponse
from utils import password_hash

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: Returns a message to show successful execution
    """
    return {"message": "The api works"}


@app.post(
    "/posts",
    status_code=status.HTTP_201_CREATED,
    response_model=PostResponse
)
async def create_post(_post: PostCreate, _db: Session = Depends(get_db)):
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

    return _new_post


@app.get(
    "/posts/{_id}",
    response_model=PostResponse
)
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

    return _post


@app.get(
    "/posts",
    status_code=status.HTTP_200_OK,
    response_model=List[PostResponse]
)
async def retrieve_all_posts(_db: Session = Depends(get_db)):
    """An endpoint to retrieve all the posts in the database

    Args:
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List: A list of all posts
    """
    _all_posts = _db.query(Post).all()
    return _all_posts


@app.delete(
    "/posts/{_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_post(_id: int, _db: Session = Depends(get_db)):
    """The delete Post endpoint

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


@app.put(
    "/posts/{_id}",
    status_code=status.HTTP_200_OK,
    response_model=PostResponse
)
async def update_post(_id: int, _new_post: PostCreate, _db: Session = Depends(get_db)):
    """The update endpoint for the Post

    Args:
        _id (int): The id of the Post
        _new_post (CreatePost): The update for the post
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: A 404 is raised if the post is not found

    Returns:
        dict: A dictionary containing a success message
    """
    _post_query = _db.query(Post).filter(Post.id == _id)

    _post = _post_query.first()

    if not _post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The post with id of {_id} was not found"
        )

    _post_query.update(_new_post.dict())

    _db.commit()

    return _post_query.first()


@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse
)
async def create_user(_new_user: UserRequest, _db: Session = Depends(get_db)):
    """An endpoint to create Users

    Args:
        _new_user (UserBase): The new user info
        _db (Session, optional): The database connection. Defaults to Depends(get_db).

    Returns:
        UserBase: The newly created user
    """
    # Hashing the password
    _hashed_password = password_hash(_new_user.password)
    _new_user.password = _hashed_password

    _user = User(**_new_user.dict())
    _db.add(_user)
    _db.commit()
    _db.refresh(_user)

    return _user


@app.get("/users/{_id}", response_model=UserResponse)
async def retrieve_one_user(_id: int, _db: Session = Depends(get_db)) -> UserResponse:
    """An endpoint to retrieve one user

    Args:
        _id (int): The id of the user
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: A 404 is raised if the user is not found in the database

    Returns:
        UserResponse: User data formatted in the User Response schema is given back
    """
    _user = _db.query(User).filter(User.id == _id).first()

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with id {_id} not found"
        )

    return _user
