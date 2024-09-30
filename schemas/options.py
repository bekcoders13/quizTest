from pydantic import BaseModel, Field


class CreateOptions(BaseModel):
    name: str
    science_id: int = Field(..., gt=0)
