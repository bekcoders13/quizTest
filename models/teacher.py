from db import Base
from sqlalchemy import Column, String, Integer, Text


class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    about = Column(Text, nullable=False)



