import inspect
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from functions.answers import get_answers_f, create_answer_f, update_answer_f, delete_answer_f
from models.answer import Answers
from models.question import Questions
from routes.login import get_current_active_user
from utils.db_operations import get_in_db
from utils.role_verification import role_verification
from schemas.answers import CreateAnswer, UpdateAnswer
from schemas.user import CreateUser
from db import database


answers_router = APIRouter(
    prefix="/answers",
    tags=["Javoblar"]
)


@answers_router.get('/get')
async def get_answer(question_id: int = 0, ident: int = 0, page: int = Query(1),
                     limit: int = Query(25), db: Session = Depends(database),
                     current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    if question_id:
        await get_in_db(db, Questions, question_id)
        return db.query(Answers).filter(Answers.question_id == question_id).all()

    return get_answers_f(ident, page, limit, db)


@answers_router.post('/create')
async def add_answer(form: List[CreateAnswer], db: Session = Depends(database),
                     current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_answer_f(form, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@answers_router.put("/update")
async def update_answer(form: UpdateAnswer, db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_answer_f(form, db)
    raise HTTPException(status_code=200, detail="Update Success !!!")


@answers_router.delete("/delete")
async def delete_answer(ident: int = 0, db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_answer_f(ident, db)
    raise HTTPException(status_code=200, detail="Delete Success !!!")
