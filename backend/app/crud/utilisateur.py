from sqlalchemy.orm import Session
from  app.models import model
from app.schemas import schema


# CRUD UTILISATEUR

# Afficher un seule Utilisateur
def get_utilisateur(db: Session, utilisateur_id: int):
    return db.query(model.Utilisateur).filter(model.Utilisateur.id == utilisateur_id).first()

#Afficher Tous les Utilisateur
def get_utilisateurs(db: Session):
    return db.query(model.Utilisateur).all()

# Creation Utilisateur
def create_utilisateur(db: Session, utilisateur: schema.UtilisateurCreate):
    db_utilisateur = model.Utilisateur(**utilisateur.dict())
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur


# modifier Utilisateur
def update_utilisateur(db: Session, utilisateur_id: int, utilisateur: schema.UtilisateurUpdate):
    db_utilisateur = get_utilisateur(db, utilisateur_id)
    if db_utilisateur:
        for key, value in utilisateur.dict().items():
            setattr(db_utilisateur, key, value)
        db.commit()
        db.refresh(db_utilisateur)
    return db_utilisateur

# Suppression Utilisateur
def delete_user(db: Session, user_id: int):
    db_utilisateur = get_utilisateurs(db, user_id)
    if db_utilisateur:
        db.delete(db_utilisateur)
        db.commit()
    return db_utilisateur
