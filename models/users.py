from db import Base
from sqlalchemy import Column, String, Integer


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lastname = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=True)
    birthdate = Column(String(50), nullable=True)
    region = Column(String(255), nullable=True)
    town = Column(String(255), nullable=True)
    role = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
