from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def get_in_db(
        db: Session,
        model,
        ident: int
):
    obj = db.query(model).get(ident)
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bazada bunday {model} yoq"
        )
    return obj


def save_in_db(db, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
