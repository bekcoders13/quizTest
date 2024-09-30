from sqlalchemy import Column, Integer, Text, DateTime, Boolean
from sqlalchemy.orm import relationship

from db import Base
from models.sms_logs import SmsLogs


class ErrorLogs(Base):
    __tablename__ = "error_logs"
    id = Column(Integer, autoincrement=True, primary_key=True)
    error_message = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    sms_log_id = Column(Integer, nullable=False)

    sms_log = relationship('SmsLogs', foreign_keys=True,
                           primaryjoin=lambda: SmsLogs.id == ErrorLogs.sms_log_id)
