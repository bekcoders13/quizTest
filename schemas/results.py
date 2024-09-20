from pydantic import BaseModel, Field


class CreateResult(BaseModel):
    found: int
    option_id: int = Field(..., gt=0)
    user_id: int = Field(..., gt=0)


class UpdateResult(BaseModel):
    ident: int = Field(..., gt=0)
    found: int
    option_id: int = Field(..., gt=0)
    user_id: int = Field(..., gt=0)
