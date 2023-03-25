"""A file that has a bunch of random utils"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def password_hash(password: str):
    return pwd_context.hash(password)
