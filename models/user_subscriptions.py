from sqlalchemy import Column, Integer, Double, Boolean, DateTime
from sqlalchemy.orm import relationship

from db import Base
from models.plans import Plans
from models.users import Users


class UserSubscript(Base):
    __tablename__ = 'user_subscriptions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)
    plan_id = Column(Integer, nullable=False)

    user = relationship('Users', foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == UserSubscript.user_id)

    plan = relationship('Plans', foreign_keys=[plan_id],
                        primaryjoin=lambda: Plans.id == UserSubscript.plan_id)
