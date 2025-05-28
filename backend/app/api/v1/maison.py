from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import maison
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/maisons",
    tags=["Maisons"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Maison

@router.get("/{maison_id}", response_model=schema.MaisonRead)
def read_maison(maison_id: int, db: Session = Depends(get_db)):
    db_Maison = maison.get_maison(db, maison_id)
    if db_Maison is None:
        raise HTTPException(status_code=404, detail="maison not found")
    return db_Maison



@router.get("/", response_model=list[schema.MaisonRead])
def lister_Maison(db: Session = Depends(get_db)):
    return maison.get_maisons(db)


@router.post("/", response_model=schema.MaisonRead)
def creer_Maison(maisons: schema.MaisonCreate, db: Session = Depends(get_db)):
    return maison.create_maison(db, maisons)


@router.put("/{maison_id}", response_model=schema.MaisonRead)
def update__Maison(maison_id: int, maisons: schema.MaisonUpdate, db: Session = Depends(get_db)):
    db_maison = maison.update_maison(db, maison_id, maisons)
    if db_maison is None:
        raise HTTPException(status_code=404, detail="maison not found")
    return db_maison

@router.delete("/{maison_id}", response_model=schema.MaisonRead)
def delete__Maison(maison_id: int, db: Session = Depends(get_db)):
    db_maison = maison.delete_maison(db, maison_id)
    if db_maison is None:
        raise HTTPException(status_code=404, detail="maison not found")
    return db_maison