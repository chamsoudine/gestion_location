from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import chambre
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/chambres",
    tags=["Chambres"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Chambre

@router.get("/{Chambre_id}", response_model=schema.ChambreRead)
def read_Chambre(Chambre_id: int, db: Session = Depends(get_db)):
    db_Chambre = chambre.get_Chambre(db, Chambre_id)
    if db_Chambre is None:
        raise HTTPException(status_code=404, detail="Chambre not found")
    return db_Chambre



@router.get("/", response_model=list[schema.ChambreRead])
def lister_Chambre(db: Session = Depends(get_db)):
    return chambre(db)


@router.post("/", response_model=schema.ChambreRead)
def creer_Chambre(Chambres: schema.ChambreCreate, db: Session = Depends(get_db)):
    return chambre.create_Chambre(db, Chambres)


@router.put("/{Chambre_id}", response_model=schema.ChambreRead)
def update__Chambre(Chambre_id: int, Chambres: schema.ChambreUpdate, db: Session = Depends(get_db)):
    db_Chambre = chambre.update_Chambre(db, Chambre_id, Chambres)
    if db_Chambre is None:
        raise HTTPException(status_code=404, detail="Chambre not found")
    return db_Chambre

@router.delete("/{Chambre_id}", response_model=schema.ChambreRead)
def delete__Chambre(Chambre_id: int, db: Session = Depends(get_db)):
    db_Chambre = chambre.delete_Chambre(db, Chambre_id)
    if db_Chambre is None:
        raise HTTPException(status_code=404, detail="Chambre not found")
    return db_Chambre