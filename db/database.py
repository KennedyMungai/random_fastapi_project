from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from os.path import dirname, join
from dotenv import find_dotenv, load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}'
