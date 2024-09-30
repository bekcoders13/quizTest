import inspect
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from functions.categories import get_categories_f, update_category_f, create_category_f, delete_category_f
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.categories import CreateCategory, UpdateCategory
from schemas.user import CreateUser
from db import database


categories_router = APIRouter(
    prefix="/categories",
    tags=["Kategoriyalar"]
)


@categories_router.get('/get')
async def get_category(ident: int = 0, db: AsyncSession = Depends(database),
                       current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    item = await get_categories_f(ident, db)
    return item


@categories_router.post('/create')
async def create_category(form: List[CreateCategory], db: AsyncSession = Depends(database),
                          current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await create_category_f(form, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@categories_router.put("/update")
async def update_category(forms: List[UpdateCategory], db: AsyncSession = Depends(database),
                          current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await update_category_f(forms, db)
    raise HTTPException(status_code=200, detail="Update Success !!!")


@categories_router.delete("/delete")
async def delete_category(ident: int = 0, db: AsyncSession = Depends(database),
                          current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await delete_category_f(ident, db)
    raise HTTPException(status_code=200, detail="Delete Success !!!")
