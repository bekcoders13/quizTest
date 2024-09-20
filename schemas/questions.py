from pydantic import BaseModel, Field


class CreateQuestion(BaseModel):
    text: str
    option_id: int = Field(..., gt=0)


class UpdateQuestion(BaseModel):
    id: int = Field(..., gt=0)
    text: str
    option_id: int = Field(..., gt=0)
