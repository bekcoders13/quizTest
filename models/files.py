from sqlalchemy import Column, Integer, String, and_, Text
from sqlalchemy.orm import relationship, backref

from db import Base
from models.course import Courses
from models.option import Options
from models.science import Sciences
from models.user import Users


class Files(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, autoincrement=True)
    new_files = Column(Text, nullable=False, unique=True)
    source = Column(String(55), nullable=False)
    source_id = Column(Integer, nullable=False)

    science = relationship(argument="Sciences", foreign_keys=[source_id], viewonly=True,
                           primaryjoin=lambda: and_(Sciences.id == Files.source_id,
                                                    Files.source == "science"),
                           backref=backref("files"))

    user = relationship(argument="Users", foreign_keys=[source_id], viewonly=True,
                        primaryjoin=lambda: and_(Users.id == Files.source_id,
                                                 Files.source == "user"),
                        backref=backref("files"))

    course = relationship(argument="Courses", foreign_keys=[source_id], viewonly=True,
                          primaryjoin=lambda: and_(Courses.id == Files.source_id,
                                                   Files.source == "course"),
                          backref=backref("files"))

    option = relationship(argument="Options", foreign_keys=[source_id], viewonly=True,
                          primaryjoin=lambda: and_(Options.id == Files.source_id,
                                                   Files.source == "option"),
                          backref=backref("files"))
