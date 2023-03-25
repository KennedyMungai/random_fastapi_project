"""Stores all the authentication logic for the API"""
from fastapi import APIRouter, Depends, status, HTTPException, Response


login_router = APIRouter(prefix="/login", tags=["Authentication"])
