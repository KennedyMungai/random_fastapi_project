"""File contains JWT logic and stuff"""
import os

from dotenv import find_dotenv, load_dotenv
from jose import JWTError, jwt

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRATION_TIME = 30
