from sqlalchemy.orm import joinedload, load_only
from models.sciences import Sciences
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.questions import Questions


def get_question_f(ident, science_id, level, page, limit, db):
    if ident > 0:
        ident_filter = Questions.id == ident
    else:
        ident_filter = Questions.id > 0

    if science_id > 0:
        science_filter = Questions.science_id == science_id
    else:
        science_filter = Questions.id > 0

    if level:
        search_formatted = "%{}%".format(level)
        search_filter = Questions.level.like(search_formatted)
    else:
        search_filter = Questions.id > 0

    items = (db.query(Questions).options(load_only(Questions.question, Questions.level)).
             filter(ident_filter, science_filter, search_filter).
             order_by(Questions.id.desc()))
    return pagination(items, page, limit)


def create_question_f(forms, db):
    for form in forms:
        get_in_db(db, Sciences, form.science_id)
        new_item_db = Questions(
            question=form.question,
            level=form.level,
            science_id=form.science_id
        )
        save_in_db(db, new_item_db)


def update_question_f(form, db):
    get_in_db(db, Sciences, form.science_id)
    get_in_db(db, Questions, form.id)
    db.query(Questions).filter(Questions.id == form.id).update({
        Questions.question: form.question,
        Questions.science_id: form.science_id,
        Questions.level: form.level,
    })
    db.commit()


def delete_question_f(ident, db):
    get_in_db(db, Questions, ident)
    db.query(Questions).filter(Questions.id == ident).delete()
    db.commit()
