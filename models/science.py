from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base
from models.category import Categories


class Sciences(Base):
    __tablename__ = "sciences"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, nullable=False)

    category = relationship('Categories', foreign_keys=[category_id],
                            primaryjoin=lambda: Categories.id == Sciences.category_id)
