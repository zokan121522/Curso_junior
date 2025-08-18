from fastapi import FastAPI, Depends
from auth import router as auth_router          # 👈 sin punto si estás en misma carpeta
from auth_utils import get_current_user         # 👈 sin punto también

app = FastAPI()

app.include_router(auth_router)                 # 👈 Esto activa /register y /login

@app.get("/")
def inicio():
    return {"mensaje": "🚀 API funcionando correctamente"}

@app.get("/perfil")
def perfil(usuario: str = Depends(get_current_user)):
    return {"mensaje": f"👤 Bienvenido, {usuario}"}

# Ruta protegida con get_current_user y JWT
from fastapi import Depends

@app.get("/perfil")
def perfil(usuario: str = Depends(get_current_user)):
    return {"mensaje": f"👤 Bienvenido, {usuario}"}
