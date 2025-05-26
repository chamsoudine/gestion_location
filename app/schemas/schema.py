import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime



# Schéma de base pour création/mise à jour
class MaisonBase(BaseModel):
    proprietaire_id: int
    adresse: Optional[str]
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]
    description: Optional[str]

# Schéma pour création
class MaisonCreate(MaisonBase):
    pass

# Schéma pour mise à jour (optionnel)
class MaisonUpdate(MaisonBase):
    pass

# Schéma pour lecture simple
class MaisonRead(MaisonBase):
    id: int
    cree_le: datetime

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }


# Schéma de base pour création/mise à jour
class ChambreBase(BaseModel):
    maison_id: int
    titre: Optional[str]
    description: Optional[str]
    taille: Optional[str]  # ex: "12m²"
    type: Optional[str]    # "simple", "appartement" ou "maison"
    meublee: Optional[bool]
    salle_de_bain: Optional[bool]
    prix: Optional[Decimal]
    disponible: Optional[bool]

# Schéma pour création
class ChambreCreate(ChambreBase):
    pass

# Schéma pour mise à jour (optionnel)
class ChambreUpdate(ChambreBase):
    pass

# Schéma pour lecture simple
class ChambreRead(ChambreBase):
    id: int
    cree_le: datetime

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }        


class ContratBase(BaseModel):
    locataire_id: int
    chambre_id: int
    date_debut: Optional[datetime]
    date_fin: Optional[datetime]
    montant_caution: Optional[Decimal]
    mois_caution: Optional[int]  # <= 3 selon commentaire SQL
    description: Optional[str]
    mode_paiement: Optional[str]  # virement | cash | mobile money
    periodicite: Optional[str]    # journalier | hebdomadaire | mensuel
    statut: Optional[str]         # actif | resilié

class ContratCreate(ContratBase):
    pass

class ContratUpdate(ContratBase):
    pass

class ContratRead(ContratBase):
    id: int
    cree_le: datetime

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }        



class PaiementBase(BaseModel):
    contrat_id: int
    montant: Optional[Decimal]
    statut: Optional[str]        # payé | impayé
    date_echeance: Optional[datetime]
    date_paiement: datetime

class PaiementCreate(PaiementBase):
    pass

class PaiementUpdate(PaiementBase):
    pass

class PaiementRead(PaiementBase):
    id: int
    cree_le: datetime

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }  


class RendezVousBase(BaseModel):
    locataire_id: int
    chambre_id: int
    date_heure: datetime
    statut: Optional[str]  # en_attente | confirmé | annulé

class RendezVousCreate(RendezVousBase):
    pass

class RendezVousUpdate(RendezVousBase):
    pass

class RendezVousRead(RendezVousBase):
    id: int
    cree_le: datetime

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }        


class MediaBase(BaseModel):
    chambre_id: int
    url: Optional[str]
    type: Optional[str]  # photo | video
    description: Optional[str]

class MediaCreate(MediaBase):
    pass

class MediaUpdate(MediaBase):
    pass

class MediaRead(MediaBase):
    id: int
    cree_le: datetime

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }


class ProblemeBase(BaseModel):
    contrat_id: int
    signale_par: Optional[int]  # utilisateur_id
    description: Optional[str]
    type: Optional[str]         # plomberie | electricite | autre
    responsable: Optional[str]  # locataire | proprietaire
    resolu: Optional[bool]

class ProblemeCreate(ProblemeBase):
    pass

class ProblemeUpdate(ProblemeBase):
    pass

class ProblemeRead(ProblemeBase):
    id: int
    cree_le: datetime

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }       

# ✅ Schéma de base pour création/mise à jour
class UtilisateurBase(BaseModel):
    nom_utilisateur: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    cni: Optional[str] = None
    role: Optional[str] = Field(default=None, description="proprietaire ou locataire")

# ✅ Pour la création
class UtilisateurCreate(UtilisateurBase):
    pass

# ✅ Pour la mise à jour
class UtilisateurUpdate(UtilisateurBase):
    pass

# ✅ Pour les réponses (lecture)
class UtilisateurRead(UtilisateurBase):
    id: int
    cree_le: datetime

    maisons: List[MaisonRead] = []
    contrats: List[ContratRead] = []
    rendez_vous: List[RendezVousRead] = []
    problemes_signales: List[ProblemeRead] = []

    model_config = {
        "from_attributes": True  # équivalent de `orm_mode` en Pydantic v2
    }    