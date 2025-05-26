from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD MAISON

# Afficher une seule Maison
def get_maison(db: Session, maison_id: int):
    return db.query(model.Maison).filter(model.Maison.id == maison_id).first()

#Afficher Tous les maison
def get_maisons(db: Session):
    return db.query(model.Maison).all()

# Creation maison
def create_maison(db: Session, maison: schema.MaisonCreate):
    db_maison = model.Maison(**maison.dict())
    db.add(db_maison)
    db.commit()
    db.refresh(db_maison)
    return db_maison


# modifier maison
def update_maison(db: Session, maison_id: int, maison: schema.MaisonUpdate):
    db_maison = get_maison(db, maison_id)
    if db_maison:
        for key, value in maison.dict().items():
            setattr(db_maison, key, value)
        db.commit()
        db.refresh(db_maison)
    return db_maison

# Suppression maison
def delete_maison(db: Session, maison_id: int):
    db_maison = get_maison(db, maison_id)
    if db_maison:
        db.delete(db_maison)
        db.commit()
    return db_maison
