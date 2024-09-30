from sqlalchemy import Column, Integer, String, DateTime

from db import Base


class SmsVerification(Base):
    __tablename__ = "sms_verification"
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(20), nullable=False)
    verification_code = Column(String(10), nullable=False)
    expires_at = Column(DateTime, nullable=False)
