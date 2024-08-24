from pydantic import BaseModel, Field


class CreateScience(BaseModel):
    name: str
    category_id: int = Field(..., gt=0)


class UpdateScience(BaseModel):
    id: int = Field(..., gt=0)
    name: str
    category_id: int = Field(..., gt=0)

