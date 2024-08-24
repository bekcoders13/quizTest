from models.comments import Comments
from models.questions import Questions
from utils.db_operations import get_in_db, save_in_db


def create_comment_f(forms, db):
    for form in forms:
        get_in_db(db, Questions, form.question_id)
        item = Comments(
            comment_text=form.comment_text,
            question_id=form.question_id
        )
        save_in_db(db, item)


def update_comment_f(form, db):
    get_in_db(db, Comments, form.ident)
    db.query(Comments).filter(Comments.id == form.ident).update({
        Comments.comment_text: form.comment_text
    })
    db.commit()


def delete_comment_f(ident, db):
    get_in_db(db, Comments, ident)
    db.query(Comments).filter(Comments.id == ident).delete()
    db.commit()
