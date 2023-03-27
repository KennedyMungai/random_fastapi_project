"""The Users routing information"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from db.database import get_db
from models.models import User
from schemas.user_schemas import UserRequest, UserResponse
from utils import password_hash
from oauth2 import get_current_user


users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse
)
async def create_user(
        _new_user: UserRequest,
        _db: Session = Depends(get_db),
        _get_current_user: int = Depends(get_current_user)
):
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


@ users_router.get(
    "/{_id}",
    response_model=UserResponse
)
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
