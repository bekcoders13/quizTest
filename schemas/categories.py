from pydantic import BaseModel, Field


class CreateCategory(BaseModel):
    name: str


class UpdateCategory(BaseModel):
    id: int = Field(..., gt=0)
    name: str
