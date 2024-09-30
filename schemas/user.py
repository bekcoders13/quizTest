from enum import Enum
from pydantic import BaseModel, validator, Field

from models.user import Users
from db import SessionLocal

db = SessionLocal()


class CreateUser(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    password: str
    birthdate: str
    gender: str
    region: str
    town: str

    @validator('phone_number')
    def username_validate(cls, phone_number):
        validate_my = db.query(Users).filter(
            Users.phone_number == phone_number,
        ).count()

        if validate_my != 0:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        return phone_number

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 belgidan kam bo`lmasligi kerak')
        return password


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    password: str
    birthdate: str
    gender: str
    region: str
    town: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 belgidan kam bo`lmasligi kerak')
        return password


class RoleType(str, Enum):
    user = 'user'
    admin = 'admin'
    editor = 'editor'


class UpdateRole(BaseModel):
    ident: int = Field(..., gt=0)
    role: RoleType
