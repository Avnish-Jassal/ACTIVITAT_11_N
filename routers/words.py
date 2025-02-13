from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/palabras/", response_model=list[schemas.PalabraResponse])
def obtener_palabras(db: Session = Depends(get_db)):
    return crud.get_palabras(db)
