"""File contains JWT logic and stuff"""
import os
from datetime import datetime, timedelta

from dotenv import find_dotenv, load_dotenv
from jose import JWTError, jwt

from schemas.user_schemas import TokenData

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

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_TIME)
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
        _payload = jwt.decode(_token, SECRET_KEY, ALGORITHM)
        _id: str = _payload.get("user_id")

        if not _id:
            raise _credentials_exception

        _token_data = TokenData(id=_id)
    except JWTError:
        raise _credentials_exception
