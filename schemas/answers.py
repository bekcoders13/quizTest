from pydantic import BaseModel


class CreateAnswer(BaseModel):
    text: str
    status: bool
    question_id: int


class UpdateAnswer(BaseModel):
    id: int
    text: str
    status: bool
    question_id: int
