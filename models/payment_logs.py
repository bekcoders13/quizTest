from sqlalchemy import Column, Integer, DateTime, Text

from db import Base


class PaymentLogs(Base):
    __tablename__ = 'payment_logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    request_body = Column(Text, nullable=False)
    response_body = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    transaction_id = Column(Integer, nullable=False)
