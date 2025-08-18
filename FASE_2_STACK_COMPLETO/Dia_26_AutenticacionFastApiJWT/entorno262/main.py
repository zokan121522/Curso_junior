# 📍 snippet ⇒ mod-auth-main-app
# FastAPI app principal con rutas /, /register, /login y /perfil protegida con JWT 📂 ├── main.py
from fastapi import FastAPI
from auth import router as auth_router          # 👈 sin punto si estás en misma carpeta
from auth_utils import get_current_user         # 👈 sin punto también

app = FastAPI()

app.include_router(auth_router)                 # 👈 Esto activa /register y /login

@app.get("/")
def inicio():
    return {"mensaje": "🚀 API funcionando correctamente"}

# Ruta protegida con get_current_user y JWT 📂 ├──main.py
# 📍 Snippet: mod-auth-protected
from fastapi import Depends

@app.get("/perfil")
def perfil(usuario: str = Depends(get_current_user)):
    return {"mensaje": f"👤 Bienvenido, {usuario}"}