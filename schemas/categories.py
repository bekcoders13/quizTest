from pydantic import BaseModel, Field


class CreateCategory(BaseModel):
    name: str
    science_id: int = Field(..., gt=0)


class UpdateCategory(BaseModel):
    id: int = Field(..., gt=0)
    name: str
    science_id: int = Field(..., gt=0)
