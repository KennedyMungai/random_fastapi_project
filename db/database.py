"""The database connection file"""
import os

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())

DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

DB_URL = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
