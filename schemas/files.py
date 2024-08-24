from typing import List
from enum import Enum
from fastapi import UploadFile
from pydantic import BaseModel, Field


class SourceType(Enum):
    question = 'question'
    answer = "answer"
    comment = "comment"


class CreateFiles(BaseModel):
    source: SourceType
    source_id: int = Field(..., gt=0)
    new_files: List[UploadFile]
