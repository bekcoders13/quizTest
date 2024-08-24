from db import Base
from sqlalchemy import Column, String, Integer, Date


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=False)
    birthdate = Column(Date, nullable=True)
    address = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
