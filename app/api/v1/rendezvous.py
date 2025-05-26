from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import rendezvous
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/RendezVous",
    tags=["RendezVous"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# RendezVous

@router.get("/{RendezVous_id}", response_model=schema.RendezVousRead)
def read_RendezVous(RendezVous_id: int, db: Session = Depends(get_db)):
    db_RendezVous = rendezvous.get_RendezVous(db, RendezVous_id)
    if db_RendezVous is None:
        raise HTTPException(status_code=404, detail="RendezVous not found")
    return db_RendezVous



@router.get("/", response_model=list[schema.RendezVousRead])
def lister_RendezVous(db: Session = Depends(get_db)):
    return rendezvous.get_RendezVouss(db)


@router.post("/", response_model=schema.RendezVousRead)
def creer_RendezVous(RendezVouss: schema.RendezVousCreate, db: Session = Depends(get_db)):
    return rendezvous.create_RendezVous(db, RendezVouss)


@router.put("/{RendezVous_id}", response_model=schema.RendezVousRead)
def update__RendezVous(RendezVous_id: int, RendezVouss: schema.RendezVousUpdate, db: Session = Depends(get_db)):
    db_RendezVous = rendezvous.update_RendezVous(db, RendezVous_id, RendezVouss)
    if db_RendezVous is None:
        raise HTTPException(status_code=404, detail="RendezVous not found")
    return db_RendezVous

@router.delete("/{RendezVous_id}", response_model=schema.RendezVousRead)
def delete__RendezVous(RendezVous_id: int, db: Session = Depends(get_db)):
    db_RendezVous = rendezvous.delete_RendezVous(db, RendezVous_id)
    if db_RendezVous is None:
        raise HTTPException(status_code=404, detail="RendezVous not found")
    return db_RendezVous