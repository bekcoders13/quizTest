from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base
from models.sciences import Sciences


class Options(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    science_id = Column(Integer, nullable=False)

    science = relationship('Sciences', foreign_keys=[science_id],
                           primaryjoin=lambda: Sciences.id == Options.science_id)
