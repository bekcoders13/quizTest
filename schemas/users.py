from pydantic import BaseModel, validator

from models.users import Users
from db import SessionLocal

db = SessionLocal()


class CreateUser(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str
    birthdate: str
    gender: str
    region: str
    town: str

    @validator('username')
    def username_validate(cls, username):
        validate_my = db.query(Users).filter(
            Users.username == username,
        ).count()

        if validate_my != 0:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        return username

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
