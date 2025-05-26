from datetime import datetime
from sqlalchemy import DECIMAL, Column, DateTime, Integer, String, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.database import Base


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True, index=True)
    nom_utilisateur = Column(String(255))
    email = Column(String(255))
    telephone = Column(String(255))
    cni = Column(String(255))
    role = Column(String(255), comment="proprietaire | locataire")
    cree_le = Column(DateTime, default=datetime.utcnow())

    maisons = relationship("Maison", back_populates="proprietaire")
    contrats = relationship("Contrat", back_populates="locataire")
    rendez_vous = relationship("RendezVous", back_populates="locataire")
    problemes_signales = relationship("Probleme", back_populates="utilisateur")


class Maison(Base):
    __tablename__ = "maisons"

    id = Column(Integer, primary_key=True, index=True)
    proprietaire_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    adresse = Column(String(255))
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)
    description = Column(Text)
    cree_le = Column(DateTime, default=datetime.utcnow())

    proprietaire = relationship("Utilisateur", back_populates="maisons")
    chambres = relationship("Chambre", back_populates="maison")


class Chambre(Base):
    __tablename__ = "chambres"

    id = Column(Integer, primary_key=True, index=True)
    maison_id = Column(Integer, ForeignKey("maisons.id"), nullable=False)
    titre = Column(String(255))
    description = Column(Text)
    taille = Column(String(255), comment="ex: 12m²")
    type = Column(String(255), comment="simple | appartement | maison")
    meublee = Column(Boolean)
    salle_de_bain = Column(Boolean)
    prix = Column(DECIMAL)
    disponible = Column(Boolean)
    cree_le = Column(DateTime, default=datetime.utcnow())

    maison = relationship("Maison", back_populates="chambres")
    contrats = relationship("Contrat", back_populates="chambre")
    rendez_vous = relationship("RendezVous", back_populates="chambre")
    medias = relationship("Media", back_populates="chambre")



class Contrat(Base):
    __tablename__ = "contrats"

    id = Column(Integer, primary_key=True, index=True)
    locataire_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    chambre_id = Column(Integer, ForeignKey("chambres.id"), nullable=False)
    date_debut = Column(Date)
    date_fin = Column(Date)
    montant_caution = Column(DECIMAL)
    mois_caution = Column(Integer, comment="<= 3")
    description = Column(Text)
    mode_paiement = Column(String(255), comment="virement | cash | mobile money")
    periodicite = Column(String(255), comment="journalier | hebdomadaire | mensuel")
    statut = Column(String(255), comment="actif | resilié")
    cree_le = Column(DateTime, default=datetime.utcnow())

    locataire = relationship("Utilisateur", back_populates="contrats")
    chambre = relationship("Chambre", back_populates="contrats")
    problemes = relationship("Probleme", back_populates="contrat")
    paiements = relationship("Paiement", back_populates="contrat")


class Paiement(Base):
    __tablename__ = "paiements"

    id = Column(Integer, primary_key=True, index=True)
    contrat_id = Column(Integer, ForeignKey("contrats.id"), nullable=False)
    montant = Column(DECIMAL)
    statut = Column(String(255), comment="payé | impayé")
    date_echeance = Column(Date)
    date_paiement = Column(DateTime)
    cree_le = Column(DateTime, default=datetime.utcnow())

    contrat = relationship("Contrat", back_populates="paiements")

class RendezVous(Base):
    __tablename__ = "rendez_vous"

    id = Column(Integer, primary_key=True, index=True)
    locataire_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    chambre_id = Column(Integer, ForeignKey("chambres.id"), nullable=False)
    date_heure = Column(DateTime)
    statut = Column(String(255), comment="en_attente | confirmé | annulé")
    cree_le = Column(DateTime, default=datetime.utcnow())

    locataire = relationship("Utilisateur", back_populates="rendez_vous")
    chambre = relationship("Chambre", back_populates="rendez_vous")


class Media(Base):
    __tablename__ = "medias"

    id = Column(Integer, primary_key=True, index=True)
    chambre_id = Column(Integer, ForeignKey("chambres.id"), nullable=False)
    url = Column(String(255))
    type = Column(String(255), comment="photo | video")
    description = Column(Text)
    cree_le = Column(DateTime, default=datetime.utcnow())

    chambre = relationship("Chambre", back_populates="medias")    


class Probleme(Base):
    __tablename__ = "problemes"

    id = Column(Integer, primary_key=True, index=True)
    contrat_id = Column(Integer, ForeignKey("contrats.id"), nullable=False)
    signale_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True, comment="utilisateur_id")
    description = Column(Text)
    type = Column(String(255), comment="plomberie | electricite | autre")
    responsable = Column(String(255), comment="locataire | proprietaire")
    resolu = Column(Boolean)
    cree_le = Column(DateTime, default=datetime.utcnow())

    contrat = relationship("Contrat", back_populates="problemes")
    utilisateur = relationship("Utilisateur", back_populates="problemes_signales")    