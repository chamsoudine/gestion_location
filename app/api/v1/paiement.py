from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import paiement
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/paiements",
    tags=["Paiements"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Paiement

@router.get("/{Paiement_id}", response_model=schema.PaiementRead)
def read_Paiement(Paiement_id: int, db: Session = Depends(get_db)):
    db_Paiement = paiement.get_Paiement(db, Paiement_id)
    if db_Paiement is None:
        raise HTTPException(status_code=404, detail="Paiement not found")
    return db_Paiement



@router.get("/", response_model=list[schema.PaiementRead])
def lister_Paiement(db: Session = Depends(get_db)):
    return paiement.get_Paiements(db)


@router.post("/", response_model=schema.PaiementRead)
def creer_Paiement(Paiements: schema.PaiementCreate, db: Session = Depends(get_db)):
    return paiement.create_Paiement(db, Paiements)


@router.put("/{Paiement_id}", response_model=schema.PaiementRead)
def update__Paiement(Paiement_id: int, Paiements: schema.PaiementUpdate, db: Session = Depends(get_db)):
    db_Paiement = paiement.update_Paiement(db, Paiement_id, Paiements)
    if db_Paiement is None:
        raise HTTPException(status_code=404, detail="Paiement not found")
    return db_Paiement

@router.delete("/{Paiement_id}", response_model=schema.PaiementRead)
def delete__Paiement(Paiement_id: int, db: Session = Depends(get_db)):
    db_Paiement = paiement.delete_Paiement(db, Paiement_id)
    if db_Paiement is None:
        raise HTTPException(status_code=404, detail="Paiement not found")
    return db_Paiement