import inspect
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session, load_only

from functions.questions import delete_question_f
from models.category import Categories
from models.option import Options
from models.question import Questions
from models.science import Sciences
from routes.login import get_current_active_user
from schemas.options import CreateOptions
from utils.db_operations import get_in_db, save_in_db
from utils.role_verification import role_verification
from schemas.user import CreateUser
from db import database


options_router = APIRouter(
    prefix="/options",
    tags=["Variyantlar"]
)


@options_router.get('/get')
async def get_option(science_id: int, ident: int = 0, page: int = Query(1), limit: int = Query(40),
                     db: Session = Depends(database),
                     current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    offset = (page - 1) * limit
    if ident > 0:
        ident_filter = Options.id == ident
    else:
        ident_filter = Options.id > 0
    if science_id > 0:
        science_filter = Options.science_id == science_id
    else:
        science_filter = Options.id > 0
    item = (db.query(Options).options(load_only(Options.name))
            .filter(science_filter, ident_filter)
            .offset(offset).limit(limit).all())
    return item


@options_router.post("/create")
async def create_option(forms: List[CreateOptions], db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    for form in forms:
        await get_in_db(db, Sciences, form.science_id)
        item = db.query(Options).filter(Options.name == form.name, Options.science_id == form.science_id).first()
        if item:
            raise HTTPException(400, 'bu variyant mavjud')

        new_item = Options(
            name=form.name,
            science_id=form.science_id
        )
        save_in_db(db, new_item)
    raise HTTPException(200, 'Create Success')


@options_router.put('/update')
async def update_option(ident: int, option_name: str, db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await get_in_db(db, Options, ident)
    db.query(Options).filter(Options.id == ident).update({
        Options.name: option_name
    })
    db.commit()
    raise HTTPException(200, 'Update, Success')


@options_router.delete('/delete')
async def delete_option(ident: int, db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    await get_in_db(db, Options, ident)
    questions = db.query(Questions).filter(Questions.option_id == ident).all()
    for question in questions:
        delete_question_f(question.ident, db)
    db.query(Options).filter(Options.id == ident).delete()
    db.commit()
    raise HTTPException(200, 'variyant savollari va javoblari bilan ochirildi')
