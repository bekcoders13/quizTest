import inspect
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from models.app_about import AppAbout
from routes.login import get_current_active_user
from utils.db_operations import save_in_db
from utils.role_verification import role_verification
from schemas.user import CreateUser
from db import database


app_about_router = APIRouter(
    prefix="/settings",
    tags=["Sozlamalar, ilova haqida"]
)


@app_about_router.get('/get')
async def get_app_about(db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    item = db.query(AppAbout).all()
    return item


@app_about_router.post('/create')
async def add_urls(telegram: str, instagram: str, web_url: str,
                   db: AsyncSession = Depends(database),
                   current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    new_item = AppAbout(
        telegram=telegram,
        instagram=instagram,
        web_url=web_url
    )
    save_in_db(db, new_item)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@app_about_router.put("/update")
async def update_urls(ident: int, telegram: str, instagram: str, web_url: str,
                      db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    db.query(AppAbout).filter(AppAbout.id == ident).update({
        AppAbout.telegram: telegram,
        AppAbout.instagram: instagram,
        AppAbout.web_url: web_url
    })
    db.commit()
    raise HTTPException(status_code=200, detail="Update Success !!!")
