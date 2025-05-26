from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import media
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/medias",
    tags=["Medias"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Media

@router.get("/{Media_id}", response_model=schema.MediaRead)
def read_Media(Media_id: int, db: Session = Depends(get_db)):
    db_Media = media.get_Media(db, Media_id)
    if db_Media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return db_Media



@router.get("/", response_model=list[schema.MediaRead])
def lister_Media(db: Session = Depends(get_db)):
    return media.get_Medias(db)


@router.post("/", response_model=schema.MediaRead)
def creer_Media(Medias: schema.MediaCreate, db: Session = Depends(get_db)):
    return media.create_Media(db, Medias)


@router.put("/{Media_id}", response_model=schema.MediaRead)
def update__Media(Media_id: int, Medias: schema.MediaUpdate, db: Session = Depends(get_db)):
    db_Media = media.update_Media(db, Media_id, Medias)
    if db_Media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return db_Media

@router.delete("/{Media_id}", response_model=schema.MediaRead)
def delete__Media(Media_id: int, db: Session = Depends(get_db)):
    db_Media = media.delete_Media(db, Media_id)
    if db_Media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return db_Media