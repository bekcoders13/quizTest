import os
from datetime import datetime
import aiofiles

from models.files import Files
from fastapi import HTTPException, UploadFile
from utils.db_operations import save_in_db, get_in_db


def save_file_db(source, source_id, name, filename, db):
    get_in_db(db, source, source_id)
    new_db = Files(
        new_files=filename,
        source_id=source_id,
        source=name
    )
    save_in_db(db, new_db)


async def save_file(file: UploadFile) -> str:
    if not file.filename.lower().endswith((".png", ".jpg", ".jpeg", ".mp4", '.pdf')):
        raise HTTPException(status_code=400, detail="Fayl formati mos emas")

    _, file_extension = os.path.splitext(file.filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_filename = f"{timestamp}{file_extension}"
    image_path = os.path.join('files', unique_filename)

    async with aiofiles.open(image_path, "wb") as buffer:
        await buffer.write(await file.read())
    return unique_filename


def delete_file_f(file_id: int, db):
    file_info = db.query(Files).filter(Files.id == file_id).first()
    if not file_info:
        raise HTTPException(status_code=404, detail="Fayl topilmadi")
    path = f"./files/{file_info.new_files}"
    # faylni o'zini o'chirish
    os.remove(path)
    # faylni bazadan o'chirish
    db.query(Files).filter(Files.id == file_id).delete()
    db.commit()
