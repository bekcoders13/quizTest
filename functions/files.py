import os
from models.files import Files
from fastapi import HTTPException


def create_file_f(model, name, new_files, ident, db):
    if db.query(model).filter(model.id == ident).first() is None:
        raise HTTPException(400, "Fayl biriktiriladigan ma'lumot topilmadi !!!")
    uploaded_file_objects = []
    for new_file in new_files:
        ext = os.path.splitext(new_file.filename)[-1].lower()
        if ext not in [".jpg", ".png", ".mp3", ".mp4", ".gif", ".jpeg"]:
            raise HTTPException(400, "Fayl formati mos kelmadi !!!")
        file_location = f"files/{new_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(new_file.file.read())

        new_db = Files(
            new_files=new_file.filename,
            source_id=ident,
            source=name
        )
        uploaded_file_objects.append(new_db)
    db.add_all(uploaded_file_objects)
    db.commit()


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
