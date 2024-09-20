from utils.db_operations import get_in_db, save_in_db
from models.categories import Categories


async def get_categories_f(ident, science_id, db):
    if ident > 0:
        ident_filter = Categories.id == ident
    else:
        ident_filter = Categories.id > 0
    if science_id > 0:
        science_filter = Categories.science_id == science_id
    else:
        science_filter = Categories.id > 0
    return db.query(Categories).filter(ident_filter, science_filter).order_by(Categories.id.desc()).all()


async def create_category_f(forms, db):
    for form in forms:
        new_item_db = Categories(
            name=form.name,
            science_id=form.science_id
        )
        save_in_db(db, new_item_db)


async def update_category_f(forms, db):
    for form in forms:
        await get_in_db(db, Categories, form.id)
        db.query(Categories).filter(Categories.id == form.id).update({
            Categories.name: form.name,
            Categories.science_id: form.science_id
        })
        db.commit()


async def delete_category_f(ident, db):
    await get_in_db(db, Categories, ident)
    db.query(Categories).filter(Categories.id == ident).delete()
    db.commit()


