from utils.db_operations import get_in_db, save_in_db
from models.category import Categories


async def get_categories_f(ident, db):
    if ident > 0:
        ident_filter = Categories.id == ident
    else:
        ident_filter = Categories.id > 0

    return db.query(Categories).filter(ident_filter).order_by(Categories.id.desc()).all()


async def create_category_f(forms, db):
    for form in forms:
        new_item_db = Categories(
            name=form.name
        )
        save_in_db(db, new_item_db)


async def update_category_f(forms, db):
    for form in forms:
        await get_in_db(db, Categories, form.id)
        db.query(Categories).filter(Categories.id == form.id).update({
            Categories.name: form.name
        })
        db.commit()


async def delete_category_f(ident, db):
    await get_in_db(db, Categories, ident)
    db.query(Categories).filter(Categories.id == ident).delete()
    db.commit()
