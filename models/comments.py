from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base
from models.questions import Questions


class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment_text = Column(String, nullable=False)
    question_id = Column(Integer, nullable=False)

    question = relationship("Questions", foreign_keys=[question_id],
                            primaryjoin=lambda: Questions.id == Comments.question_id)
