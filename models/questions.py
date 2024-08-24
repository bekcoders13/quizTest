from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer
from models.sciences import Sciences


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(255), nullable=False)
    level = Column(String(255), nullable=False)
    science_id = Column(Integer, nullable=False)

    science = relationship("Sciences", foreign_keys=[science_id],
                           primaryjoin=lambda: Sciences.id == Questions.science_id)
