from models.answers import Answers
from utils.db_operations import get_in_db, save_in_db
from models.questions import Questions


def get_answers_f(ident, page, limit, db):
    offset_value = (page - 1) * limit
    if ident > 0:
        ident_filter = Answers.id == ident
    else:
        ident_filter = Answers.id > 0

    return (db.query(Answers).filter(ident_filter).order_by(Answers.id.desc())
            .offset(offset_value).limit(limit).all())


def create_answer_f(forms, db):
    for form in forms:
        get_in_db(db, Questions, form.question_id)
        new_item_db = Answers(
            text=form.text,
            status=form.status,
            question_id=form.question_id
        )
        save_in_db(db, new_item_db)


def update_answer_f(form, db):
    get_in_db(db, Questions, form.question_id), get_in_db(db, Answers, form.id)
    db.query(Answers).filter(Answers.id == form.id).update({
        Answers.text: form.text,
        Answers.status: form.status,
        Answers.question_id: form.question_id
    })
    db.commit()


def delete_answer_f(ident, db):
    get_in_db(db, Answers, ident)
    db.query(Answers).filter(Answers.id == ident).delete()
    db.commit()


