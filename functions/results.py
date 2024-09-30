from models.finalresult import FinalResults
from models.result import Results
from utils.db_operations import save_in_db

from sqlalchemy.exc import SQLAlchemyError


async def add_result_f(form, db):
    try:
        item_db = db.query(Results).filter(
            Results.option_id == form.option_id,
            Results.user_id == form.user_id
        ).first()

        user_item = db.query(FinalResults).filter(FinalResults.user_id == form.user_id).first()

        if item_db:
            db.query(Results).filter(
                Results.user_id == form.user_id,
                Results.option_id == form.option_id
            ).update({Results.found: form.found})

            db.query(FinalResults).filter(FinalResults.user_id == form.user_id).update({
                FinalResults.common: FinalResults.common - item_db.found + form.found
            })
        else:
            new_item_db = Results(
                found=form.found,
                option_id=form.option_id,
                user_id=form.user_id
            )
            save_in_db(db, new_item_db)

            if user_item:
                db.query(FinalResults).filter(FinalResults.id == user_item.id).update({
                    FinalResults.common: FinalResults.common + form.found
                })
            else:
                new_item = FinalResults(
                    common=form.found,
                    user_id=form.user_id
                )
                save_in_db(db, new_item)

        db.commit()
        return {"status": "success"}

    except SQLAlchemyError as e:
        db.rollback()
        return {"status": "error", "message": str(e)}
