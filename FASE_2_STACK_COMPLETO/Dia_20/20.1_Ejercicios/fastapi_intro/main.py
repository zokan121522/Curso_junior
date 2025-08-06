from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/saludo")
def saludar():
    return{"mensaje": "Hola desde servidor"}

class Perfil(BaseModel):
    nombre : str
    edad : int

@app.post("/perfil")
def recibir_perfil(perfil:Perfil):
    return{
        "mensaje": f"Perfil recibido de {perfil.nombre}, edad{perfil.edad}"
    }

