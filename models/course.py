from db import Base
from sqlalchemy import Column, String, Integer, Text


class Courses(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    about = Column(Text, nullable=False)
