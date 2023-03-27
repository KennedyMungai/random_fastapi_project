"""The file contains the information on the posts route"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from db.database import get_db
from models.models import Post
from oauth2 import get_current_user
from schemas.post_schemas import PostCreate, PostResponse

posts_router = APIRouter(prefix="/posts", tags=["Posts"])


@posts_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=PostResponse
)
async def create_post(
    _post: PostCreate,
    _db: Session = Depends(get_db),
    _user=Depends(get_current_user)
):
    """The create post endpoint

    Args:
        _post (CreatePost): The new post
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the created post
    """
    _new_post = Post(user_id=_user.id, **_post.dict())

    _db.add(_new_post)
    _db.commit()
    _db.refresh(_new_post)

    return _new_post


@posts_router.get(
    "/{_id}",
    response_model=PostResponse
)
async def retrieve_one_post(
    _id: int,
    _db: Session = Depends(get_db),
    _user=Depends(get_current_user)
) -> Post:
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


@posts_router.get(
    "/",
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


@posts_router.delete(
    "/{_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_post(
    _id: int,
    _db: Session = Depends(get_db),
    _user=Depends(get_current_user)
):
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


@posts_router.put(
    "/{_id}",
    status_code=status.HTTP_200_OK,
    response_model=PostResponse
)
async def update_post(
    _id: int,
    _new_post: PostCreate,
    _db: Session = Depends(get_db),
    _user=Depends(get_current_user)
):
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
