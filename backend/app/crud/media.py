from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD Media

# Afficher une seule Media
def get_Media(db: Session, Media_id: int):
    return db.query(model.Media).filter(model.Media.id == Media_id).first()

#Afficher Tous les Media
def get_Medias(db: Session):
    return db.query(model.Media).all()

# Creation Media
def create_Media(db: Session, Media: schema.MediaCreate):
    db_Media = model.Media(**Media.dict())
    db.add(db_Media)
    db.commit()
    db.refresh(db_Media)
    return db_Media


# modifier Media
def update_Media(db: Session, Media_id: int, Media: schema.MediaUpdate):
    db_Media = get_Media(db, Media_id)
    if db_Media:
        for key, value in Media.dict().items():
            setattr(db_Media, key, value)
        db.commit()
        db.refresh(db_Media)
    return db_Media

# Suppression Media
def delete_Media(db: Session, Media_id: int):
    db_Media = get_Media(db, Media_id)
    if db_Media:
        db.delete(db_Media)
        db.commit()
    return db_Media
