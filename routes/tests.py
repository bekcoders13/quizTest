import inspect
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, load_only

from models.answer import Answers
from models.question import Questions
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.user import CreateUser
from db import database


tests_router = APIRouter(
    prefix="/test",
    tags=["Testlar"]
)


@tests_router.get('/get_tests')
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
