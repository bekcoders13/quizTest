from models.category import Categories
from utils.db_operations import get_in_db, save_in_db
from models.science import Sciences

from sqlalchemy.orm import load_only
from sqlalchemy import desc


def get_science_f(ident, category_id, page, limit, db):
    offset_value = (page - 1) * limit
    if ident > 0:
        ident_filter = Sciences.id == ident
    else:
        ident_filter = Sciences.id > 0
    if category_id > 0:
        category_filter = Sciences.category_id == category_id
    else:
        category_filter = Sciences.id > 0

    items = (db.query(Sciences)
             .filter(ident_filter, category_filter).order_by(desc(Sciences.id))
             .offset(offset_value).limit(limit).all())
    return items


def create_science_f(forms, db):
    for form in forms:
        get_in_db(db, Categories, form.category_id)
        new_item_db = Sciences(
            name=form.name,
            category_id=form.category_id,
        )
        save_in_db(db, new_item_db)


def update_science_f(form, db):
    get_in_db(db, Sciences, form.id)
    db.query(Sciences).filter(Sciences.id == form.id).update({
        Sciences.name: form.name
    })
    db.commit()


def delete_science_f(ident, db):
    get_in_db(db, Sciences, ident)
    db.query(Sciences).filter(Sciences.id == ident).delete()
    db.commit()
