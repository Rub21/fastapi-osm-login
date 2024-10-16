from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db

from schemas.user import UserCreate
from utils.user_crud import create_user

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
