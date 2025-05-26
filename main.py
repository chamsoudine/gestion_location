# main.py
from fastapi import FastAPI
from app.api.v1.routes import api_router

app = FastAPI(title="API de gestion de location de chambres")

app.include_router(api_router)