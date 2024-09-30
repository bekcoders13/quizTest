import inspect
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, joinedload

from functions.course import get_course_f, update_course_f, create_course_f, delete_course_f
from models.connection_courses import Connections
from models.course import Courses
from models.teacher import Teachers
from routes.login import get_current_active_user
from utils.db_operations import get_in_db, save_in_db
from utils.role_verification import role_verification
from schemas.course import CreateCourse, UpdateCourse, CreateComposition
from schemas.user import CreateUser
from db import database


courses_router = APIRouter(
    prefix="/courses",
    tags=["Kurslar"]
)


@courses_router.get('/get')
async def get_course(ident: int = 0, db: AsyncSession = Depends(database),
                     current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    item = await get_course_f(ident, db)
    return item


@courses_router.post('/create')
async def create_course(form: List[CreateCourse], db: AsyncSession = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await create_course_f(form, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@courses_router.put("/update")
async def update_course(forms: List[UpdateCourse], db: AsyncSession = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await update_course_f(forms, db)
    raise HTTPException(status_code=200, detail="Update Success !!!")


@courses_router.delete("/delete")
async def delete_course(ident: int = 0, db: AsyncSession = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await delete_course_f(ident, db)
    raise HTTPException(status_code=200, detail="Delete Success !!!")


@courses_router.post('/create_composition')
async def create_composition(form: CreateComposition, db: AsyncSession = Depends(database),
                             current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await get_in_db(db, Courses, form.course_id)
    await get_in_db(db, Teachers, form.teacher_id)
    new_item_db = Connections(
        teacher_id=form.teacher_id,
        course_id=form.course_id,
        composition=form.composition,
        duration=form.duration
    )
    save_in_db(db, new_item_db)
    raise HTTPException(200, 'Create Success')


@courses_router.get('/get_composition')
async def get_composition(course_id: int, db: Session = Depends(database),
                          current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    items = (db.query(Connections).options(joinedload(Connections.teacher))
             .filter(Connections.course_id == course_id).all())
    return items
