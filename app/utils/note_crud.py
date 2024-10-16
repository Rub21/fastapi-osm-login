from sqlalchemy.orm import Session
from models.note import  Note
from schemas.note import NoteCreate


def create_note(db: Session, note: NoteCreate, user_id: int):
    db_note = Note(content=note.content, user_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note