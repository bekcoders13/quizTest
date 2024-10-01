import inspect
import os
import re
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException

from db import database
from functions.files import delete_file_f, save_file, save_file_db
from models.course import Courses
from models.files import Files
from models.option import Options
from models.science import Sciences
from models.user import Users
from routes.login import get_current_active_user
from schemas.files import CreateFiles, SourceType
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

    source_model_mapping = {
        SourceType.option: Options,
        SourceType.science: Sciences,
        SourceType.course: Courses,
        SourceType.user: Users
    }

    source_model = source_model_mapping.get(form.source)
    if source_model:
        save_file_db(source_model, form.source_id, form.source.value, filename, db)

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

    if not re.match(r'^[\w,\s-]+\.[A-Za-z]{3,4}$', fileName):
        raise HTTPException(status_code=400, detail="Noto'g'ri fayl nomi")

    path = os.path.abspath(os.path.join('files', fileName))

    if os.path.isfile(path):
        return FileResponse(path, media_type='application/octet-stream', filename=fileName)
    else:
        raise HTTPException(status_code=404, detail="Fayl topilmadi")


@files_router.delete("/delete_file")
async def delete_file(ident: int, db: Session = Depends(database),
                      c_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(c_user, inspect.currentframe().f_code.co_name)
    delete_file_f(ident, db)
    raise HTTPException(200, "Success !!!")
