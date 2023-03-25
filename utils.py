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


def verify_password(_plain_password: str, _hashed_password: str) -> bool:
    """A function to compare the plain password with the hashed password

    Args:
        _plain_password (str): _description_
        _hashed_password (str): _description_

    Returns:
        bool: _description_
    """
    return pwd_context.verify(_plain_password, _hashed_password)
