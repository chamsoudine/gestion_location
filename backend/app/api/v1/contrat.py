from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import contrat
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/contrats",
    tags=["Contrats"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Contrat

@router.get("/{Contrat_id}", response_model=schema.ContratRead)
def read_Contrat(Contrat_id: int, db: Session = Depends(get_db)):
    db_Contrat = contrat.get_Contrat(db, Contrat_id)
    if db_Contrat is None:
        raise HTTPException(status_code=404, detail="Contrat not found")
    return db_Contrat



@router.get("/", response_model=list[schema.ContratRead])
def lister_Contrat(db: Session = Depends(get_db)):
    return contrat.get_Contrats(db)


@router.post("/", response_model=schema.ContratRead)
def creer_Contrat(Contrats: schema.ContratCreate, db: Session = Depends(get_db)):
    return contrat.create_Contrat(db, Contrats)


@router.put("/{Contrat_id}", response_model=schema.ContratRead)
def update__Contrat(Contrat_id: int, Contrats: schema.ContratUpdate, db: Session = Depends(get_db)):
    db_Contrat = contrat.update_Contrat(db, Contrat_id, Contrats)
    if db_Contrat is None:
        raise HTTPException(status_code=404, detail="Contrat not found")
    return db_Contrat

@router.delete("/{Contrat_id}", response_model=schema.ContratRead)
def delete__Contrat(Contrat_id: int, db: Session = Depends(get_db)):
    db_Contrat = contrat.delete_Contrat(db, Contrat_id)
    if db_Contrat is None:
        raise HTTPException(status_code=404, detail="Contrat not found")
    return db_Contrat