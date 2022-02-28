import string
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,DateTime,Integer
from datetime import datetime


Base = declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer(), primary_key=True)
    username=Column(String(25), nullable=True, unique=True)
    email=Column(string(80),unique=True, nullable=True)
    date=Column(DateTime(),default=datetime.utcnow)
    
    
