from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base
from models.categories import Categories


class Options(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, nullable=False)

    category = relationship('Categories', foreign_keys=[category_id],
                            primaryjoin=lambda: Categories.id == Options.category_id)
