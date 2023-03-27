"""File contains JWT logic and stuff"""
import os
from datetime import datetime, timedelta

from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm.session import Session

from db.database import get_db
from schemas.user_schemas import TokenData
from models.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRATION_TIME = 30


def create_access_token(_data: dict):
    """The function that created the access token

    Args:
        _data (dict): The data to be encoded

    Returns:
        _type_: The encoded jwt
    """
    _to_encode = _data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_TIME)
    _to_encode.update({"exp": expire})

    _encoded_jwt = jwt.encode(_to_encode, SECRET_KEY, ALGORITHM)

    return _encoded_jwt


def verify_access_token(_token: str, _credentials_exception):
    """A function to verify the access token

    Args:
        _token (str): The access token
        _credentials_exception (Exception): The passed in exception

    Raises:
        _credentials_exception: The exception passed in
    """
    try:
        _payload = jwt.decode(_token, SECRET_KEY, algorithms=[ALGORITHM])
        _id: str = _payload.get("user_id")

        if not _id:
            raise _credentials_exception

        _token_data = TokenData(id=_id)
    except JWTError as _e:
        raise _credentials_exception + " " + _e

    return _token_data


def get_current_user(
        _token: str = Depends(oauth2_scheme),
        _db: Session = Depends(get_db)
):
    """Gets the current user

    Args:
        _token (str, optional): The access token. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: Access token verification
    """
    _credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    token = verify_access_token(_token, _credentials_exception)

    _user = _db.query(User).filter(User.id == token.id).first()

    return _user
