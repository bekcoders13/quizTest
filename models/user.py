from db import Base
from sqlalchemy import Column, String, Integer, DateTime


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lastname = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=True)
    birthdate = Column(String(50), nullable=True)
    region = Column(String(255), nullable=True)
    town = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    role = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
