from pydantic import BaseModel, Field


class CreateTeacher(BaseModel):
    name: str
    about: str


class UpdateTeacher(CreateTeacher):
    id: int = Field(..., gt=0)
