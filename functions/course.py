from utils.db_operations import get_in_db, save_in_db
from models.course import Courses


async def get_course_f(ident, db):
    if ident > 0:
        ident_filter = Courses.id == ident
    else:
        ident_filter = Courses.id > 0

    return db.query(Courses).filter(ident_filter).order_by(Courses.id.desc()).all()


async def create_course_f(forms, db):
    for form in forms:
        new_item_db = Courses(
            name=form.name,
            about=form.about
        )
        save_in_db(db, new_item_db)


async def update_course_f(forms, db):
    for form in forms:
        await get_in_db(db, Courses, form.id)
        db.query(Courses).filter(Courses.id == form.id).update({
            Courses.name: form.name,
            Courses.about: form.about
        })
        db.commit()


async def delete_course_f(ident, db):
    await get_in_db(db, Courses, ident)
    db.query(Courses).filter(Courses.id == ident).delete()
    db.commit()
