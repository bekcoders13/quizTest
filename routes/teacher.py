import inspect
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from functions.teacher import get_teacher_f, create_teacher_f, update_teacher_f, delete_teacher_f
from routes.login import get_current_active_user
from schemas.teacher import CreateTeacher, UpdateTeacher
from utils.role_verification import role_verification
from schemas.user import CreateUser
from db import database


teachers_router = APIRouter(
    prefix="/teachers",
    tags=["O'qituvchilar"]
)


@teachers_router.get('/get')
async def get_teacher(ident: int = 0, db: AsyncSession = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    item = await get_teacher_f(ident, db)
    return item


@teachers_router.post('/create')
async def create_teacher(form: List[CreateTeacher], db: AsyncSession = Depends(database),
                         current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await create_teacher_f(form, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@teachers_router.put("/update")
async def update_teacher(forms: List[UpdateTeacher], db: AsyncSession = Depends(database),
                         current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await update_teacher_f(forms, db)
    raise HTTPException(status_code=200, detail="Update Success !!!")


@teachers_router.delete("/delete")
async def delete_teacher(ident: int = 0, db: AsyncSession = Depends(database),
                         current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await delete_teacher_f(ident, db)
    raise HTTPException(status_code=200, detail="Delete Success !!!")
