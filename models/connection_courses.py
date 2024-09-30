from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Text

from db import Base
from models.course import Courses
from models.teacher import Teachers


class Connections(Base):
    __tablename__ = 'connections'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, nullable=False)
    teacher_id = Column(Integer, nullable=False)
    composition = Column(Text, nullable=False)
    duration = Column(String(100), nullable=True)

    course = relationship('Courses', foreign_keys=[course_id],
                          primaryjoin=lambda: Courses.id == Connections.course_id)

    teacher = relationship('Teachers', foreign_keys=[teacher_id],
                           primaryjoin=lambda: Teachers.id == Connections.teacher_id)
