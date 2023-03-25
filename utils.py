"""A file that has a bunch of random utils"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def password_hash(password: str) -> str:
    """A function that spits out hashed passwords

    Args:
        password (str): The password

    Returns:
        Str: A hash version of the password
    """
    return pwd_context.hash(password)
