# main.py


# 📦 1. Importamos FastAPI + herramientas extra
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

# 🚀 2. Creamos la instancia de FastAPI
app = FastAPI()

# 🧑‍🤝‍🧑 3. Simulamos una lista de usuarios
usuarios = [
{"id":  1, "nombre": "Jaime", "edad": 41},
{"id":  2, "nombre": "Jesica", "edad": 40},
{"id":  3, "nombre": "Zokan", "edad": 18},
]

# 📍 4. Ruta dinámica con parámetro: /usuario/2
@app.get("/usuario/{id}")
def obtenerUsuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return JSONResponse(content=usuario, status_code=200)
    raise HTTPException(status_code=404,detail= f"Usuario con id {id} no encontrado")
