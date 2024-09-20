from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from db import Base
from models.options import Options


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255), nullable=False)
    option_id = Column(Integer, nullable=False)

    option = relationship("Options", foreign_keys=[option_id],
                          primaryjoin=lambda: Options.id == Questions.option_id)
