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
        orm_mode = True
