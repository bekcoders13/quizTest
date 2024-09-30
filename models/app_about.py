from db import Base
from sqlalchemy import Column, String, Integer


class AppAbout(Base):
    __tablename__ = 'app_about'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram = Column(String(255), nullable=False)
    instagram = Column(String(255), nullable=False)
    web_url = Column(String(255), nullable=False)
