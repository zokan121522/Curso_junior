# 📍 Snippet⇒  mod-auth-register-json
# Registro de usuario usando Pydantic (JSON Body) 📂 ├──auth.py
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import User
from database import engine
import bcrypt
from datetime import datetime, timedelta
from pydantic import BaseModel
import jwt

router = APIRouter()

class UserRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register_user(data: UserRequest):
    hashed_pw = bcrypt.hashpw(data.password.encode("utf-8"), bcrypt.gensalt())
    user = User(username=data.username, hashed_password=hashed_pw.decode("utf-8"))

    with Session(engine) as session:
        session.add(user)
        session.commit()
    return {"message": "✅ Usuario registrado correctamente"}

# 📍Snippet: mod-auth-login
# 🔐 Login y generación de token JWT 📂 ├──auth.py

SECRET_KEY = "clave-secreta"  # ⚠️ Cambiar en producción

@router.post("/login")
def login(data: UserRequest):
    with Session(engine) as session:
        statement = select(User).where(User.username == data.username)
        user = session.exec(statement).first()

    if not user or not bcrypt.checkpw(data.password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    payload = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=60)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}