from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer
from models.user import Users


class Results(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    found = Column(Integer, nullable=False)
    option_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Results.user_id)
