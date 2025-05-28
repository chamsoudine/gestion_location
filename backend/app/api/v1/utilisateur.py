from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schema
from app.crud  import utilisateur
#from app.models import model
from app.db.database import engine, SessionLocal, Base


router = APIRouter(
    prefix="/utilisateurs",
    tags=["Utilisateurs"]
)

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utilisateur

@router.get("/{user_id}", response_model=schema.UtilisateurRead)
def read_utilisateur(user_id: int, db: Session = Depends(get_db)):
    db_utilisateur = utilisateur.get_utilisateur(db, user_id)
    if db_utilisateur is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_utilisateur



@router.get("/", response_model=list[schema.UtilisateurRead])
def lister_utilisateur(db: Session = Depends(get_db)):
    return utilisateur.get_utilisateurs(db)


@router.post("/", response_model=schema.UtilisateurRead)
def creer_utilisateur(user: schema.UtilisateurCreate, db: Session = Depends(get_db)):
    return utilisateur.create_utilisateur(db, user)


@router.put("/{user_id}", response_model=schema.UtilisateurRead)
def update__utilisateur(user_id: int, user: schema.UtilisateurUpdate, db: Session = Depends(get_db)):
    db_user = utilisateur.update_utilisateur(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=schema.UtilisateurRead)
def delete__utilisateur(user_id: int, db: Session = Depends(get_db)):
    db_user = utilisateur.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user