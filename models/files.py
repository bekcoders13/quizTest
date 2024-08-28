from sqlalchemy import Column, Integer, String, and_, Text
from sqlalchemy.orm import relationship, backref

from db import Base
from models.answers import Answers
from models.comments import Comments
from models.questions import Questions


class Files(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, autoincrement=True)
    new_files = Column(Text, nullable=False, unique=True)
    source = Column(String(55), nullable=False)
    source_id = Column(Integer, nullable=False)

    question = relationship(argument="Questions", foreign_keys=[source_id], viewonly=True,
                            primaryjoin=lambda: and_(Questions.id == Files.source_id,
                                                     Files.source == "question"),
                            backref=backref("files"))
    answer = relationship(argument="Answers", foreign_keys=[source_id], viewonly=True,
                          primaryjoin=lambda: and_(Answers.id == Files.source_id,
                                                   Files.source == "answer"),
                          backref=backref("files"))
