import inspect
import os
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException

from db import database
from functions.files import delete_file_f, save_file, save_file_db
from models.answer import Answers
from models.files import Files
from models.question import Questions
from routes.login import get_current_active_user
from schemas.files import CreateFiles
from schemas.user import CreateUser
from utils.role_verification import role_verification

files_router = APIRouter(
    prefix="/files",
    tags=["Fayllar bilan ishlash"]
)


@files_router.post("/upload_file")
async def create_file(form: CreateFiles = Depends(CreateFiles),
                      db: Session = Depends(database),
                      c_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(c_user, inspect.currentframe().f_code.co_name)
    filename = await save_file(form.new_files)
    if form.source == "question":
        await save_file_db(Questions, form.source_id, 'question', filename, db)
    elif form.source == "answer":
        await save_file_db(Answers, form.source_id, 'answer', filename, db)
    raise HTTPException(200, "Create Success!!!")


@files_router.get("/get_files")
async def get_db_file(db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    return db.query(Files).all()


@files_router.get('/files/{fileName}')
async def get_file(fileName: str,
                   c_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(c_user, inspect.currentframe().f_code.co_name)
    path = f"./files/{fileName}"
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(400, "Not Found")


@files_router.delete("/delete_file")
async def delete_file(ident: int, db: Session = Depends(database),
                      c_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(c_user, inspect.currentframe().f_code.co_name)
    delete_file_f(ident, db)
    raise HTTPException(200, "Success !!!")
