from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer
from models.answers import Answers
from models.questions import Questions
from models.sciences import Sciences
from models.users import Users


class Results(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, nullable=False)
    answer_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    science_id = Column(Integer, nullable=False)

    question = relationship("Questions", foreign_keys=[question_id],
                            primaryjoin=lambda: Questions.id == Results.question_id)

    answer = relationship("Answers", foreign_keys=[answer_id],
                          primaryjoin=lambda: Answers.id == Results.answer_id)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Results.user_id)

    sciences = relationship("Sciences", foreign_keys=[science_id],
                            primaryjoin=lambda: Sciences.id == Results.science_id)
