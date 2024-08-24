from sqlalchemy.orm import load_only

from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.sciences import Sciences


def get_science_f(ident, category_id, page, limit, db):
    if ident > 0:
        ident_filter = Sciences.id == ident
    else:
        ident_filter = Sciences.id > 0

    if category_id > 0:
        category_filter = Sciences.category_id == category_id
    else:
        category_filter = Sciences.id > 0

    items = (db.query(Sciences).options(load_only(Sciences.name)).
             filter(ident_filter, category_filter).order_by(Sciences.id.desc()))
    return pagination(items, page, limit)


def create_science_f(forms, db):
    for form in forms:
        new_item_db = Sciences(
            name=form.name,
            category_id=form.category_id,
        )
        save_in_db(db, new_item_db)


def update_science_f(form, db):
    get_in_db(db, Sciences, form.id)
    db.query(Sciences).filter(Sciences.id == form.id).update({
        Sciences.name: form.name,
        Sciences.category_id: form.category_id,
    })
    db.commit()


def delete_science_f(ident, db):
    get_in_db(db, Sciences, ident)
    db.query(Sciences).filter(Sciences.id == ident).delete()
    db.commit()


