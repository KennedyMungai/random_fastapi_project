"""File contains JWT logic and stuff"""
import os
from datetime import datetime, timedelta

from dotenv import find_dotenv, load_dotenv
from jose import JWTError, jwt

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
