from pydantic import BaseModel, Field


class CreateCourse(BaseModel):
    name: str
    about: str


class UpdateCourse(CreateCourse):
    id: int = Field(..., gt=0)


class CreateComposition(BaseModel):
    teacher_id: int = Field(..., gt=0)
    course_id: int = Field(..., gt=0)
    composition: str
    duration: str
