import inspect
from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session, joinedload

from db import database
from functions.comments import create_comment_f, update_comment_f, delete_comment_f
from models.comments import Comments
from models.questions import Questions
from routes.login import get_current_active_user
from schemas.comments import CreateComment, UpdateComment
from schemas.users import CreateUser
from utils.role_verification import role_verification

comments_router = APIRouter(prefix="/comments", tags=["Comments operations"])


@comments_router.post("/create")
def create_comment(forms: List[CreateComment], db: Session = Depends(database),
                   c_user: CreateUser = Depends(get_current_active_user)):
    role_verification(c_user, inspect.currentframe().f_code.co_name)
    create_comment_f(forms, db)
    raise HTTPException(200, "Create Success!!!")


@comments_router.get("/get")
def get_comment(question_id: int = 0, ident: int = 0, page: int = Query(1), limit: int = Query(25),
                db: Session = Depends(database),
                c_user: CreateUser = Depends(get_current_active_user)):
    role_verification(c_user, inspect.currentframe().f_code.co_name)
    if question_id:
        return (db.query(Comments).
                options(joinedload(Comments.files), joinedload(Comments.question).load_only(Questions.question)).
                filter(Comments.question_id == question_id).all())
    if ident:
        return (db.query(Comments).options(joinedload(Comments.files)).
                filter(Comments.id == ident).first())
    return db.query(Comments).order_by(Comments.id.desc()).offset(page).limit(limit).all()


@comments_router.put("/update")
def update_comment(form: UpdateComment, db: Session = Depends(database),
                   c_user: CreateUser = Depends(get_current_active_user)):
    role_verification(c_user, inspect.currentframe().f_code.co_name)
    update_comment_f(form, db)
    raise HTTPException(200, "Update Success!!!")


@comments_router.delete("/delete")
def delete_comment(ident: int, db: Session = Depends(database),
                   c_user: CreateUser = Depends(get_current_active_user)):
    role_verification(c_user, inspect.currentframe().f_code.co_name)
    delete_comment_f(ident, db)
    raise HTTPException(200, "Delete Success!!!")
