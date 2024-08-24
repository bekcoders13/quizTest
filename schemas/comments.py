from pydantic import BaseModel, Field


class CreateComment(BaseModel):
    comment_text: str
    question_id: int = Field(..., gt=0)


class UpdateComment(BaseModel):
    ident: int = Field(..., gt=0)
    comment_text: str
