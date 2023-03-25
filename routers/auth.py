"""Stores all the authentication logic for the API"""
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm.session import Session

from db.database import get_db
from models.models import User
from schemas.UserLogin import UserLogin
from utils import verify_password


login_router = APIRouter(prefix="/login", tags=["Authentication"])


@login_router.post("/")
async def login(_user_credentials: UserLogin, _db: Session = Depends(get_db)):
    _user = _db.query(User).filter(
        User.email == _user_credentials.email).first()

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )

    if not verify_password(_user_credentials.password, _user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
