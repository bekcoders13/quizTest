from pydantic import BaseModel, Field


class CreateScience(BaseModel):
    name: str


class UpdateScience(BaseModel):
    id: int = Field(..., gt=0)
    name: str
