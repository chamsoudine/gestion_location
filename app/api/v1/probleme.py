from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import probleme
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/problemes",
    tags=["Problemes"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Probleme

@router.get("/{Probleme_id}", response_model=schema.ProblemeRead)
def read_Probleme(Probleme_id: int, db: Session = Depends(get_db)):
    db_Probleme = probleme.get_Probleme(db, Probleme_id)
    if db_Probleme is None:
        raise HTTPException(status_code=404, detail="Probleme not found")
    return db_Probleme



@router.get("/", response_model=list[schema.ProblemeRead])
def lister_Probleme(db: Session = Depends(get_db)):
    return probleme.get_Problemes(db)


@router.post("/", response_model=schema.ProblemeRead)
def creer_Probleme(Problemes: schema.ProblemeCreate, db: Session = Depends(get_db)):
    return probleme.create_Probleme(db, Problemes)


@router.put("/{Probleme_id}", response_model=schema.ProblemeRead)
def update__Probleme(Probleme_id: int, Problemes: schema.ProblemeUpdate, db: Session = Depends(get_db)):
    db_Probleme = probleme.update_Probleme(db, Probleme_id, Problemes)
    if db_Probleme is None:
        raise HTTPException(status_code=404, detail="Probleme not found")
    return db_Probleme

@router.delete("/{Probleme_id}", response_model=schema.ProblemeRead)
def delete__Probleme(Probleme_id: int, db: Session = Depends(get_db)):
    db_Probleme = probleme.delete_Probleme(db, Probleme_id)
    if db_Probleme is None:
        raise HTTPException(status_code=404, detail="Probleme not found")
    return db_Probleme