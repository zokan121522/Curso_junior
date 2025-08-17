# main.py

from fastapi import FastAPI
from models import User
from database import engine

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "🚀 API funcionando correctamente"}