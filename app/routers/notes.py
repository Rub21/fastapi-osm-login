from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from utils.note_crud import create_note
from schemas.note import NoteCreate
router = APIRouter()

@router.post("/notes/", response_model=NoteCreate)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_note(db=db, note=note, user_id=current_user.id)
