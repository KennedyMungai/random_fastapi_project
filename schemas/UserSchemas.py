"""The file that contains User Schemas"""
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Created the Base class for the User data

    Args:
        BaseModel (Class): The parent class for the UserBase
    """
    id: int
    email: EmailStr
    password: str


class UserRequest(UserBase):
    """The user request schema

    Args:
        UserBase (Class): The base user type
    """


class UserResponse(BaseModel):
    """The response model for the user

    Args:
        BaseModel (Class): The parent class
    """
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        """The config class for the UserResponse class"""
        orm_mode = True
