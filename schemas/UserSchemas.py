"""The file that contains User Schemas"""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Created the Base class for the User data

    Args:
        BaseModel (Class): The parent class for the UserBase
    """
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
    email: EmailStr

    class Config:
        """The config class for the UserResponse class"""
        orm_mode = True
