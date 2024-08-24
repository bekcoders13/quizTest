from pydantic import BaseModel, Field


class CreateQuestion(BaseModel):
    question: str
    level: str
    science_id: int = Field(..., gt=0)


class UpdateQuestion(BaseModel):
    id: int = Field(..., gt=0)
    question: str
    level: str
    science_id: int = Field(..., gt=0)
