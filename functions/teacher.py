from utils.db_operations import get_in_db, save_in_db
from models.teacher import Teachers


async def get_teacher_f(ident, db):
    if ident > 0:
        ident_filter = Teachers.id == ident
    else:
        ident_filter = Teachers.id > 0

    return db.query(Teachers).filter(ident_filter).order_by(Teachers.id.desc()).all()


async def create_teacher_f(forms, db):
    for form in forms:
        new_item_db = Teachers(
            name=form.name,
            about=form.about
        )
        save_in_db(db, new_item_db)


async def update_teacher_f(forms, db):
    for form in forms:
        await get_in_db(db, Teachers, form.id)
        db.query(Teachers).filter(Teachers.id == form.id).update({
            Teachers.name: form.name,
            Teachers.about: form.about
        })
        db.commit()


async def delete_teacher_f(ident, db):
    await get_in_db(db, Teachers, ident)
    db.query(Teachers).filter(Teachers.id == ident).delete()
    db.commit()


