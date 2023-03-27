"""Stores all the authentication logic for the API"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from db.database import get_db
from models.models import User
from oauth2 import create_access_token
from utils import verify_password

login_router = APIRouter(prefix="/login", tags=["Authentication"])


@login_router.post("/")
async def login(_user_credentials: OAuth2PasswordRequestForm = Depends(), _db: Session = Depends(get_db)):
    """Created the login endpoint

    Args:
        _user_credentials (UserLogin): The details required for user authentication
        _db (Session, optional): A database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: A 404 is returned is not found
        HTTPException: A 404 is returned if 
                        the password of a found user does not match the hash stored in the database

    Returns:
        Dict: A message to show successful execution of the login in the endpoint
    """
    _user = _db.query(User).filter(
        User.email == _user_credentials.username).first()

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )

    if not verify_password(_user_credentials.password, _user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )

    # Create a token
    # Return token

    _access_token = create_access_token({"user_id": _user.id})

    return {"access_token": _access_token, "token_type": "bearer"}
