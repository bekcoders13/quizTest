from sqlalchemy import Column, Integer, DateTime, Double, String

from db import Base


class Plans(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Double, nullable=False)
    duration_days = Column(DateTime, nullable=False)
