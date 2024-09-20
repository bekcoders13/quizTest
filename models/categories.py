from sqlalchemy.orm import relationship

from db import Base
from sqlalchemy import Column, String, Integer

from models.sciences import Sciences


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    science_id = Column(Integer, nullable=False)

    science = relationship("Sciences", foreign_keys=[science_id],
                           primaryjoin=lambda: Sciences.id == Categories.science_id)

