"""File contains JWT logic and stuff"""
import os

from dotenv import find_dotenv, load_dotenv
from jose import JWTError, jwt

_env = load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")
