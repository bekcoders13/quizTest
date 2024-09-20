from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from db import Base
from models.users import Users


class FinalResults(Base):
    __tablename__ = 'finalresults'
    id = Column(Integer, primary_key=True, autoincrement=True)
    common = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == FinalResults.user_id)
