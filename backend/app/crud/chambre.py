from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD Chambre

# Afficher une seule Chambre
def get_Chambre(db: Session, Chambre_id: int):
    return db.query(model.Chambre).filter(model.Chambre.id == Chambre_id).first()

#Afficher Tous les Chambre
def get_Chambres(db: Session):
    return db.query(model.Chambre).all()

# Creation Chambre
def create_Chambre(db: Session, Chambre: schema.ChambreCreate):
    db_Chambre = model.Chambre(**Chambre.dict())
    db.add(db_Chambre)
    db.commit()
    db.refresh(db_Chambre)
    return db_Chambre


# modifier Chambre
def update_Chambre(db: Session, Chambre_id: int, Chambre: schema.ChambreUpdate):
    db_Chambre = get_Chambre(db, Chambre_id)
    if db_Chambre:
        for key, value in Chambre.dict().items():
            setattr(db_Chambre, key, value)
        db.commit()
        db.refresh(db_Chambre)
    return db_Chambre

# Suppression Chambre
def delete_Chambre(db: Session, Chambre_id: int):
    db_Chambre = get_Chambre(db, Chambre_id)
    if db_Chambre:
        db.delete(db_Chambre)
        db.commit()
    return db_Chambre
