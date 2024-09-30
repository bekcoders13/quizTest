from sqlalchemy import Column, Integer, Text, DateTime, String
from sqlalchemy.orm import relationship

from db import Base
from models.users import Users


class SmsQueue(Base):
    __tablename__ = "sms_queue"
    id = Column(Integer, autoincrement=True, primary_key=True)
    message_body = Column(Text, nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship('Users', foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == SmsQueue.user_id)
