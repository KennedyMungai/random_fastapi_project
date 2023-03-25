"""The file that contains User Schemas"""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Created the Base class for the User data

    Args:
        BaseModel (Class): The parent class for the UserBase
    """
    email: EmailStr
    password: str

    class Config:
        """The config class for the UserBase class"""
        orm_mode = True
