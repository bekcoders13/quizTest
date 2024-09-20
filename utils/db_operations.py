from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


async def get_in_db(db: AsyncSession, model, ident: int):
    obj = db.get(model, ident)
    if not obj:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bazada bunday {model.__name__} yo'q")
    return obj


def save_in_db(db: Session, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
