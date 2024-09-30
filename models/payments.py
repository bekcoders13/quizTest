from sqlalchemy import Column, Integer, Double, Boolean, DateTime
from sqlalchemy.orm import relationship

from db import Base
from models.plans import Plans
from models.users import Users


class Payments(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Double, nullable=False)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)
    plan_id = Column(Integer, nullable=False)
    transaction_id = Column(Integer, nullable=False)

    user = relationship('Users', foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Payments.user_id)

    plan = relationship('Plans', foreign_keys=[plan_id],
                        primaryjoin=lambda: Plans.id == Payments.plan_id)
