from sqlalchemy import Column, Integer, Text, DateTime, Boolean
from sqlalchemy.orm import relationship

from db import Base
from models.user import Users


class SmsLogs(Base):
    __tablename__ = "sms_logs"
    id = Column(Integer, autoincrement=True, primary_key=True)
    message_body = Column(Text, nullable=False)
    provider_message_id = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)
    response_code = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship('Users', foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == SmsLogs.user_id)
