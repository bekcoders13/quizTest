import inspect
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, load_only

from models.answers import Answers
from models.options import Options
from models.questions import Questions
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.users import CreateUser
from db import database


options_router = APIRouter(
    prefix="/options",
    tags=["Testlar"]
)


@options_router.get('/get')
async def get_option(category_id: int, page: int = Query(1), limit: int = Query(40),
                     db: Session = Depends(database),
                     current_user: CreateUser = Depends(get_current_active_user)):
    await role_verification(current_user, inspect.currentframe().f_code.co_name)
    offset = (page - 1) * limit
    item = (db.query(Options).options(load_only(Options.name))
            .filter(Options.category_id == category_id)
            .offset(offset).limit(limit).all())
    return item


@options_router.get('/get_tests')
def get_test_f(option_id: int, db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)

    # Savollarni olish
    questions = (db.query(Questions).options(load_only(Questions.text))
                 .filter(Questions.option_id == option_id).all())

    # Savollar va ularning javoblarini yig'ish
    result = []
    for question in questions:
        answers = db.query(Answers).options(load_only(Answers.text, Answers.status)) \
            .filter(Answers.question_id == question.id).all()

        # Savol va javoblarni ro'yxatga qo'shish
        result.append({
            "question": question.text,
            "answers": [(answer.text, answer.status) for answer in answers]
        })

    return {f"{option_id}-variyant": result}
