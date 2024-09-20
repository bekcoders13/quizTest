from fastapi import HTTPException

from routes.login import get_password_hash
from utils.db_operations import save_in_db
from models.users import Users


async def get_user_f(ident, region, page, limit, db):
    offset_value = (page - 1) * limit
    if ident > 0:
        ident_filter = Users.id == ident
    else:
        ident_filter = Users.id > 0

    if region:
        search_formatted = "%{}%".format(region)
        search_filter = (Users.region.like(search_formatted) |
                         Users.firstname.like(search_formatted) |
                         Users.lastname.like(search_formatted))
    else:
        search_filter = Users.id > 0

    items = (db.query(Users).filter(ident_filter, search_filter).order_by(Users.id.desc())
             .offset(offset_value).limit(limit).all())
    return items


async def create_user_f(form, user, db):
    if user.role == 'admin':
        new_item_db = Users(
            firstname=form.firstname,
            lastname=form.lastname,
            username=form.username,
            gender=form.gender,
            region=form.region,
            town=form.town,
            birthdate=form.birthdate,
            role="admin",
            password=get_password_hash(form.password))
        save_in_db(db, new_item_db)
    else:
        raise HTTPException(400, "not authentication")


async def create_general_user_f(form, db):
    new_item_db = Users(
        firstname=form.firstname,
        lastname=form.lastname,
        username=form.username,
        gender=form.gender,
        region=form.region,
        town=form.town,
        birthdate=form.birthdate,
        role="user",
        password=get_password_hash(form.password))
    save_in_db(db, new_item_db)


async def update_user_f(form, db, user):
    db.query(Users).filter(Users.id == user.id).update({
        Users.firstname: form.firstname,
        Users.lastname: form.lastname,
        Users.gender: form.gender,
        Users.birthdate: form.birthdate,
        Users.region: form.region,
        Users.town: form.town,
        Users.password: get_password_hash(form.password),
    })
    db.commit()


async def delete_user_f(db, user):
    db.query(Users).filter(Users.id == user.id).delete()
    db.commit()
