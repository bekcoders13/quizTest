import inspect
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload

from functions.answers import get_answers_f, create_answer_f, update_answer_f, delete_answer_f
from models.answers import Answers
from models.questions import Questions
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.answers import CreateAnswer, UpdateAnswer
from schemas.users import CreateUser
from db import database


answers_router = APIRouter(
    prefix="/answers",
    tags=["Answers operation"]
)


@answers_router.get('/get')
def get_answer(question_id: int = 0, ident: int = 0, search: str = None,  page: int = 1,
               limit: int = 25, db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    if question_id:
        get_in_db(db, Questions, question_id)
        items = db.query(Answers).filter(Answers.question_id == question_id).all()
        random.shuffle(items)
        return items
    return get_answers_f(ident, search, page, limit, db)


@answers_router.post('/create_answer')
def create(form: List[CreateAnswer], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_answer_f(form, db)
    raise HTTPException(status_code=200, detail="Create Success !!!")


@answers_router.put("/update")
def update(form: UpdateAnswer, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_answer_f(form, db)
    raise HTTPException(status_code=200, detail="Update Success !!!")


@answers_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_answer_f(ident, db)
    raise HTTPException(status_code=200, detail="Delete Success !!!")
