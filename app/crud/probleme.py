from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD Probleme

# Afficher une seule Probleme
def get_Probleme(db: Session, Probleme_id: int):
    return db.query(model.Probleme).filter(model.Probleme.id == Probleme_id).first()

#Afficher Tous les Probleme
def get_Problemes(db: Session):
    return db.query(model.Probleme).all()

# Creation Probleme
def create_Probleme(db: Session, Probleme: schema.ProblemeCreate):
    db_Probleme = model.Probleme(**Probleme.dict())
    db.add(db_Probleme)
    db.commit()
    db.refresh(db_Probleme)
    return db_Probleme


# modifier Probleme
def update_Probleme(db: Session, Probleme_id: int, Probleme: schema.ProblemeUpdate):
    db_Probleme = get_Probleme(db, Probleme_id)
    if db_Probleme:
        for key, value in Probleme.dict().items():
            setattr(db_Probleme, key, value)
        db.commit()
        db.refresh(db_Probleme)
    return db_Probleme

# Suppression Probleme
def delete_Probleme(db: Session, Probleme_id: int):
    db_Probleme = get_Probleme(db, Probleme_id)
    if db_Probleme:
        db.delete(db_Probleme)
        db.commit()
    return db_Probleme
