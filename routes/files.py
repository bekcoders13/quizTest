import inspect
import os
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException

from db import database
from functions.files import delete_file_f, create_file_f
from models.answers import Answers
from models.comments import Comments
from models.files import Files
from models.questions import Questions
from routes.login import get_current_active_user
from schemas.files import CreateFiles
from schemas.users import CreateUser
from utils.role_verification import role_verification

files_router = APIRouter(
    prefix="/files",
    tags=["Files operations"]
)


@files_router.post("/create")
async def create_file(form: CreateFiles = Depends(CreateFiles),
                      db: Session = Depends(database),
                      c_user: CreateUser = Depends(get_current_active_user)):
    role_verification(c_user, inspect.currentframe().f_code.co_name)
    if form.source == "question":
        await create_file_f(Questions, 'question', form.new_files, form.source_id, db)
    elif form.source == "answer":
        await create_file_f(Answers, 'answer', form.new_files, form.source_id, db)
    elif form.source == "comment":
        await create_file_f(Comments, 'comment', form.new_files, form.source_id, db)
    raise HTTPException(200, "Create Success!!!")


@files_router.get("/get_files")
def get_db_file(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return db.query(Files).all()


@files_router.get('/files/{fileName}')
async def get_file(fileName: str,
                   c_user: CreateUser = Depends(get_current_active_user)):
    role_verification(c_user, inspect.currentframe().f_code.co_name)
    path = f"./files/{fileName}"
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(400, "Not Found")


@files_router.delete("/delete_file")
def delete(ident: int, db: Session = Depends(database),
           c_user: CreateUser = Depends(get_current_active_user)):
    role_verification(c_user, inspect.currentframe().f_code.co_name)
    delete_file_f(ident, db)
    raise HTTPException(200, "Success !!!")
