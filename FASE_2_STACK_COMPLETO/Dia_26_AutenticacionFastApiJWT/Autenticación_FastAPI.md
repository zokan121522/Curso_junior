
# 📚 DÍA 26 – Autenticación con FastAPI (JWT)

---

## 🎯 OBJETIVO DEL DÍA

### Aprender a crear un sistema de autenticación básico en FastAPI usando:
	• 📝 Endpoints de registro y login → Puertas de entrada y acceso.
	• 🔐 JWT (tokens) → Pase digital para acceder sin repetir tu contraseña.
	• 🧂 Hashing de contraseñas → Guardar versión cifrada de la clave.
	• 🛡️ Middleware de autorización → Guardia que revisa si tienes el pase.
	• 👁️ Validación de usuarios → Comprobación de que eres quien dices ser.
---

## 🧠 ¿QUÉ VAS A APRENDER?

### Módulo	Concepto	Tecnología/Función clave
```bash
1. Registro de usuario	Pydantic + SQLModel
2. Hashing de contraseña	bcrypt
3. Login y generación de JWT	jwt.encode con pyjwt
4. Verificación de usuario logueado	Depends(get_current_user)
```
---

## 🧩 REQUISITOS PREVIOS
	•	Tener ya una app de FastAPI funcionando.
	•	Tener SQLModel y base de datos conectada.
	•	Tener un modelo User con mínimo: id, username, hashed_password.

>Perfecto. Aquí tienes todo lo necesario organizado por archivo. Vas a montar una base mínima funcional con FastAPI, SQLModel y una tabla User, preparada para aplicar autenticación.

---

#### 📁 ESTRUCTURA BÁSICA DE ARCHIVOS
```bash
📂 tu_proyecto/
├── main.py
├── models.py
├── database.py
├── create_db.py   ← se ejecuta una sola vez para crear las tablas
```

---

#### 🧩 CONTENIDO DE CADA ARCHIVO


##### ✅ main.py
```py
from fastapi import FastAPI
from models import User
from database import engine

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "🚀 API funcionando correctamente"}
```

---

##### ✅ models.py
```py
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
```

---

##### ✅ database.py
```py
from sqlmodel import create_engine

engine = create_engine("sqlite:///db.db", echo=True)
```

---

##### ✅ create_db.py (solo se ejecuta una vez)
```py
from sqlmodel import SQLModel
from models import User
from database import engine

SQLModel.metadata.create_all(engine)
print("✅ Base de datos y tabla User creada correctamente")
```

---

#### 🚀 PASOS PARA ARRANCAR
	1.	Instala lo necesario si no lo tienes:

pip install fastapi sqlmodel uvicorn


	2.	Ejecuta este script una sola vez para crear la base de datos:

python create_db.py


	3.	Arranca el servidor:

uvicorn main:app --reload


	4.	Entra a tu navegador:

http://127.0.0.1:8000/docs





---

### 1. INSTALACIÓN DE LIBRERÍAS
```bash
pip install pyjwt bcrypt
```

---

### 2. MODELO DE USUARIO (models.py)
```py
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
```

---

### 3. REGISTRO DE USUARIO (auth.py)

#### 3.1 🔐 Hashear la contraseña
```py
import bcrypt

hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
```

#### 3.2 🧾 Guardar usuario en base de datos
```py
from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from .models import User
from .database import engine

router = APIRouter()

@router.post("/register")
def register_user(username: str, password: str):
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    user = User(username=username, hashed_password=hashed_pw.decode("utf-8"))

    with Session(engine) as session:
        session.add(user)
        session.commit()
    return {"message": "✅ Usuario registrado correctamente"}
```

---

### 4. LOGIN Y GENERACIÓN DE TOKEN (auth.py)

#### 4.1 🔑 Validar credenciales
```py
from fastapi import HTTPException

with Session(engine) as session:
    user = session.exec(
        User.select().where(User.username == username)
    ).first()

if not user or not bcrypt.checkpw(password.encode("utf-8"), user.hashed_password.encode("utf-8")):
    raise HTTPException(status_code=401, detail="Credenciales inválidas")
```

#### 4.2 🪪 Generar JWT
```py
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave-secreta"  # ⚠️ Cambiar en producción

payload = {
    "sub": user.username,
    "exp": datetime.utcnow() + timedelta(minutes=60)
}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
return {"access_token": token}
```

#### 🔁 Todo junto en `/login`
```py
@router.post("/login")
def login(username: str, password: str):
    with Session(engine) as session:
        user = session.exec(
            User.select().where(User.username == username)
        ).first()

    if not user or not bcrypt.checkpw(password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    payload = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=60)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}
```

---

### 5. PROTECCIÓN DE RUTAS (auth_utils.py)
```py
from fastapi import Depends, HTTPException, Header
from jwt import decode, exceptions

def get_current_user(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except:
        raise HTTPException(status_code=401, detail="Token inválido")
```

---

### 6. USO EN RUTAS PROTEGIDAS (main.py)
```py
from fastapi import FastAPI, Depends
from .auth import router as auth_router
from .auth_utils import get_current_user

app = FastAPI()
app.include_router(auth_router)

@app.get("/perfil")
def perfil(usuario: str = Depends(get_current_user)):
    return {"mensaje": f"👤 Bienvenido, {usuario}"}
```

---

## 🧪 TESTS BÁSICOS (opcional)

### Puedes probar en Swagger o con curl/postman:
	•	POST /register → { "username": "pepe", "password": "123" }
	•	POST /login → retorna { access_token }
	•	GET /perfil con header: Authorization: Bearer tu_token

---

## ✅ CHECKLIST DE COMPRENSIÓN
	•	¿Sabes cómo registrar un usuario y guardar contraseña encriptada?
	•	¿Entiendes cómo se genera un token JWT y cómo se protege una ruta?
	•	¿Puedes añadir Depends(get_current_user) a cualquier endpoint?
	•	¿Has probado con token válido e inválido?

---

## 📄 ARCHIVOS GENERADOS
```bash
/models.py           → Modelo User
/auth.py             → Registro + login + token
/auth_utils.py       → Validación del JWT
/main.py             → App + rutas + auth integrada
```

---

## 🧠 ANALOGÍA PARA RECORDAR

> “El registro pone una llave en una caja fuerte, el login te da una copia temporal (el token),
y el middleware comprueba si tu copia sigue siendo válida cuando entras en una habitación.”

## 🧠 CONCEPTOS CLAVE

| 📘 **Concepto**            | ⚙️ **Explicación técnica**                                                                 | 🧠 **Explicación coloquial**                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| 🔐 **JWT (JSON Web Token)** | Formato estándar para tokens de autenticación. Firmado y opcionalmente encriptado.         | 🎟️ Es como una entrada firmada al backstage: valida que eres tú sin tener que repetir el DNI cada vez.       |
| 🧂 **Hashing (bcrypt)**     | Proceso irreversible que transforma una contraseña en una cadena segura.                  | 🔒 Como guardar una contraseña cifrada que ni siquiera tú puedes ver, pero puedes comprobar si coincide.      |
| 🐍 **pyjwt**                | Librería Python para generar y verificar JWT tokens.                                       | 🧾 Una herramienta que firma y lee los pases de acceso.                                                       |
| 🧩 **Depends()**            | Sistema de inyección de dependencias de FastAPI.                                           | 🛂 Una forma automática de pasar funciones que se ejecutan antes del endpoint, como un portero de acceso.     |
| 📬 **Header()**             | Extrae información del encabezado HTTP, como el token.                                     | 🎫 Como mirar la tarjeta de invitación que trae alguien antes de dejarlo entrar.                              |
| 📦 **decode() (jwt)**       | Función que analiza el token y extrae su contenido si es válido.                          | 📖 Es como abrir un sobre sellado para leer quién lo envía y cuándo expira.                                   |
| ⌛ **ExpiredSignatureError**| Error que lanza JWT cuando el token ha caducado.                                          | 🗓️ Es como intentar usar una entrada vieja para un concierto que ya pasó.                                    |
| 🗂️ **APIRouter()**          | Permite modularizar los endpoints de FastAPI.                                             | 🧱 Divide tu API en habitaciones organizadas según su propósito.                                              |