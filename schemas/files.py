from enum import Enum
from fastapi import UploadFile
from pydantic import BaseModel, Field


class SourceType(Enum):
    course = 'course'
    science = "science"
    user = 'user'
    option = 'option'


class CreateFiles(BaseModel):
    source: SourceType
    source_id: int = Field(..., gt=0)
    new_files: UploadFile
