import inspect
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from functions.sciences import get_science_f, create_science_f, update_science_f, delete_science_f
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.sciences import CreateScience, UpdateScience
from schemas.user import CreateUser
from db import database


sciences_router = APIRouter(
    prefix="/sciences",
    tags=["Fanlar"]
)


@sciences_router.get('/get')
async def get_science(category_id: int = 0, ident: int = 0, page: int = Query(1),
                      limit: int = Query(10), db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_science_f(ident, category_id, page, limit, db)


@sciences_router.post('/create')
def create_science(form: List[CreateScience], db: Session = Depends(database),
                   current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_science_f(form, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@sciences_router.put("/update")
def update_science(form: UpdateScience, db: Session = Depends(database),
                   current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_science_f(form, db)
    raise HTTPException(status_code=200, detail="Update Success !!!")


@sciences_router.delete("/delete")
def delete_science(ident: int = 0, db: Session = Depends(database),
                   current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_science_f(ident, db)
    raise HTTPException(status_code=200, detail="Delete Success !!!")
