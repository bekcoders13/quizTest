from sqlalchemy import desc

from models.answer import Answers
from models.option import Options
from utils.db_operations import get_in_db, save_in_db
from models.question import Questions


def get_question_f(ident, db):

    if ident > 0:
        ident_filter = Questions.id == ident
    else:
        ident_filter = Questions.id > 0

    return db.query(Questions).filter(ident_filter).order_by(desc(Questions.id)).all()


def create_question_f(forms, db):
    for form in forms:
        get_in_db(db, Options, form.option_id)
        new_item_db = Questions(
            text=form.text,
            option_id=form.option_id
        )
        save_in_db(db, new_item_db)


def update_question_f(form, db):
    get_in_db(db, Options, form.option_id)
    get_in_db(db, Questions, form.id)
    db.query(Questions).filter(Questions.id == form.id).update({
        Questions.text: form.text,
        Questions.option_id: form.option_id,
    })
    db.commit()


def delete_question_f(ident, db):
    get_in_db(db, Questions, ident)
    answers = db.query(Answers).filter(Answers.question_id == ident).all()
    for answer in answers:
        db.query(Answers).filter(Answers.id == answer.id).delete()

    db.query(Questions).filter(Questions.id == ident).delete()
    db.commit()
