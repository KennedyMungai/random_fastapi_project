"""File to contain the user login schema"""
from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    """The User Login template"""
    email: EmailStr
    password: str
