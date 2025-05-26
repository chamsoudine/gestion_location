from fastapi import APIRouter
from app.api.v1 import utilisateur, maison, chambre, contrat, paiement, rendezvous, media, probleme

api_router = APIRouter()

# Inclure les sous-routers
api_router.include_router(utilisateur.router)
api_router.include_router(maison.router)
api_router.include_router(chambre.router)
api_router.include_router(contrat.router)
api_router.include_router(paiement.router)
api_router.include_router(rendezvous.router)
api_router.include_router(media.router)
api_router.include_router(probleme.router)
