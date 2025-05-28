from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD RendezVous

# Afficher une seule RendezVous
def get_RendezVous(db: Session, RendezVous_id: int):
    return db.query(model.RendezVous).filter(model.RendezVous.id == RendezVous_id).first()

#Afficher Tous les RendezVous
def get_RendezVouss(db: Session):
    return db.query(model.RendezVous).all()

# Creation RendezVous
def create_RendezVous(db: Session, RendezVous: schema.RendezVousCreate):
    db_RendezVous = model.RendezVous(**RendezVous.dict())
    db.add(db_RendezVous)
    db.commit()
    db.refresh(db_RendezVous)
    return db_RendezVous


# modifier RendezVous
def update_RendezVous(db: Session, RendezVous_id: int, RendezVous: schema.RendezVousUpdate):
    db_RendezVous = get_RendezVous(db, RendezVous_id)
    if db_RendezVous:
        for key, value in RendezVous.dict().items():
            setattr(db_RendezVous, key, value)
        db.commit()
        db.refresh(db_RendezVous)
    return db_RendezVous

# Suppression RendezVous
def delete_RendezVous(db: Session, RendezVous_id: int):
    db_RendezVous = get_RendezVous(db, RendezVous_id)
    if db_RendezVous:
        db.delete(db_RendezVous)
        db.commit()
    return db_RendezVous
