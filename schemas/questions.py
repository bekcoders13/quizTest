from pydantic import BaseModel, Field


class CreateQuestion(BaseModel):
    text: str
    level: str
    science_id: int = Field(..., gt=0)


class UpdateQuestion(BaseModel):
    id: int = Field(..., gt=0)
    text: str
    level: str
    science_id: int = Field(..., gt=0)
