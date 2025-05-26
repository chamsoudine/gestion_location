from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD Contrat

# Afficher une seule Contrat
def get_Contrat(db: Session, Contrat_id: int):
    return db.query(model.Contrat).filter(model.Contrat.id == Contrat_id).first()

#Afficher Tous les Contrat
def get_Contrats(db: Session):
    return db.query(model.Contrat).all()

# Creation Contrat
def create_Contrat(db: Session, Contrat: schema.ContratCreate):
    db_Contrat = model.Contrat(**Contrat.dict())
    db.add(db_Contrat)
    db.commit()
    db.refresh(db_Contrat)
    return db_Contrat


# modifier Contrat
def update_Contrat(db: Session, Contrat_id: int, Contrat: schema.ContratUpdate):
    db_Contrat = get_Contrat(db, Contrat_id)
    if db_Contrat:
        for key, value in Contrat.dict().items():
            setattr(db_Contrat, key, value)
        db.commit()
        db.refresh(db_Contrat)
    return db_Contrat

# Suppression Contrat
def delete_Contrat(db: Session, Contrat_id: int):
    db_Contrat = get_Contrat(db, Contrat_id)
    if db_Contrat:
        db.delete(db_Contrat)
        db.commit()
    return db_Contrat
