from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD Paiement

# Afficher un seule Paiement
def get_Paiement(db: Session, Paiement_id: int):
    return db.query(model.Paiement).filter(model.Paiement.id == Paiement_id).first()

#Afficher Tous les Paiement
def get_Paiements(db: Session):
    return db.query(model.Paiement).all()

# Creation Paiement
def create_Paiement(db: Session, Paiement: schema.PaiementCreate):
    db_Paiement = model.Paiement(**Paiement.dict())
    db.add(db_Paiement)
    db.commit()
    db.refresh(db_Paiement)
    return db_Paiement


# modifier Paiement
def update_Paiement(db: Session, Paiement_id: int, Paiement: schema.PaiementUpdate):
    db_Paiement = get_Paiement(db, Paiement_id)
    if db_Paiement:
        for key, value in Paiement.dict().items():
            setattr(db_Paiement, key, value)
        db.commit()
        db.refresh(db_Paiement)
    return db_Paiement

# Suppression Paiement
def delete_Paiement(db: Session, Paiement_id: int):
    db_Paiement = get_Paiement(db, Paiement_id)
    if db_Paiement:
        db.delete(db_Paiement)
        db.commit()
    return db_Paiement
