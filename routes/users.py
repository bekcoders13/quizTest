import inspect
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from functions.users import get_user_f, create_user_f, update_user_f, delete_user_f, create_general_user_f
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.users import CreateUser, UpdateUser
from db import database


users_router = APIRouter(
    prefix="/users",
    tags=["Foydalanuvchi operatsiyalari"]
)


@users_router.get('/get_users')
async def get(ident: int = 0, region: str = None,  page: int = Query(1),
              limit: int = Query(25), db: AsyncSession = Depends(database),
              current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    item = await get_user_f(ident, region, page, limit, db)
    return item


@users_router.get('/get_me')
async def get_me(current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    return current_user


@users_router.post('/create_admin')
async def create_admin(form: CreateUser, db: AsyncSession = Depends(database),
                       current_user: CreateUser = Depends(get_current_active_user)):
    await create_user_f(form, current_user, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@users_router.post('/sign_up')
async def create_user(form: CreateUser, db: AsyncSession = Depends(database)):
    await create_general_user_f(form, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@users_router.put("/update")
async def update_user(form: UpdateUser, db: AsyncSession = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await update_user_f(form, db, current_user)
    raise HTTPException(status_code=200, detail="Update Success !!!")


@users_router.delete("/delete")
async def delete_user(db: AsyncSession = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await delete_user_f(db, current_user)
    raise HTTPException(status_code=200, detail="Delete Success !!!")
