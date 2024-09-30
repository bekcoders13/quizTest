from pydantic import BaseModel


class Token(BaseModel):
    id: int
    access_token: str
    token_type: str


class TokenData(BaseModel):
    phone_number: str
