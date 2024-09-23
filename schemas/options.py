from pydantic import BaseModel, Field


class CreateOptions(BaseModel):
    name: str
    category_id: int = Field(..., gt=0)
