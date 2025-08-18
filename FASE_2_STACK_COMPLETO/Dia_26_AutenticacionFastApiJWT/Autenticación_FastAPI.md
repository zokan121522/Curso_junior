
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

| Módulo | Concepto                       | Tecnología / Función clave          |
|--------|--------------------------------|-------------------------------------|
| 1      | Registro de usuario            | Pydantic + SQLModel                 |
| 2      | Hashing de contraseña          | bcrypt                              |
| 3      | Login y generación de JWT      | `jwt.encode` con PyJWT              |
| 4      | Verificación de usuario logueado | `Depends(get_current_user)`        |
---

## 🧩 REQUISITOS PREVIOS
	•	Tener ya una app de FastAPI funcionando.
	•	Tener SQLModel y base de datos conectada.
	•	Tener un modelo User con mínimo: id, username, hashed_password.

>Perfecto. Aquí tienes todo lo necesario organizado por archivo. Vas a montar una base mínima funcional con FastAPI, SQLModel y una tabla User, preparada para aplicar autenticación.

---

#### 📁 ESTRUCTURA BÁSICA DE ARCHIVOS
```bash
📂 app/
├── main.py          👈 Punto de entrada principal (crea app e incluye rutas)
├── models.py        👤 Define los modelos de la base de datos (User, etc.)
├── database.py      💾 Configura la conexión con SQLite usando SQLModel
├── auth.py          🔐 Contiene los endpoints de autenticación: /register y /login
├── auth_utils.py    🔑 Valida tokens JWT para proteger rutas con Depends()
├── config.py        🔧 Configuración global (SECRET_KEY, etc.)
├── create_db.py     🛠️ Script para crear las tablas iniciales
├── requirements.txt 📋 Lista de dependencias del proyecto
```

---

#### 🧩 CONTENIDO DE CADA ARCHIVO

**Comando terminal:**  
>📍 snippet ⇒ : mod-auth-main-app

##### ✅ main.py
```py
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
```

---

##### ✅ models.py

>📍 snippet ⇒ mod-user-model

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

>📍 snippet ⇒ sqlite-engine-database

```py
from sqlmodel import create_engine

engine = create_engine("sqlite:///db.db", echo=True)
```

---

##### ✅ create_db.py (solo se ejecuta una vez)
>📍 snipet ⇒ init-db-sqlmodel-createdb
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

>🔧 Snippet: mod-user-model

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

> 📍 Snippet⇒  mod-auth-register-json

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

#### 🔁 Todo junto en `/login`
##### Esta ruta realiza 3 pasos clave:
1. **Busca al usuario** en la base de datos usando el nombre enviado.  
2. **Verifica la contraseña** comparando el texto plano con el hash usando bcrypt.  
3. **Genera un token JWT** con duración de 60 minutos y lo devuelve.

> ✅ Si todo es correcto, devuelve `{ "access_token": "..." }`.
> 🚫 Si algo falla, devuelve error `401 Credenciales inválidas`.

> 🔧 Snippet: mod-auth-login

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
> 📍 Snippet: mod-auth-utils
> 
    1.	📩 Recibe el token JWT desde la cabecera Authorization:
	2.	🔓 Descifra el token con SECRET_KEY para ver qué usuario lo firmó.
	3.	✅ Si es válido, devuelve el nombre del usuario (payload[“sub”]).
	4.	⏳ Si el token caducó, lanza error 401 Token expirado.
	5.	❌ Si es inválido o no está bien formado, lanza 401 Token inválido.

⸻

```py
# 📍 Snippet: mod-auth-utils
# 🔐 Utilidad para validar tokens JWT y extraer usuario actual 📂 ├──auth_utils.py
from config import SECRET_KEY
from fastapi import Depends, HTTPException, Header
from jwt import decode, exceptions

# 🧠 Extrae y valida el token JWT desde la cabecera Authorization
def get_current_user(authorization: str = Header(...)):
    try:
        # 🔍 Separa el token del prefijo "Bearer"
        token = authorization.split(" ")[1]

        # 🔓 Decodifica el token con la clave secreta
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])

        # ✅ Devuelve el nombre de usuario si todo va bien
        return payload["sub"]

    # ⏰ Si el token está caducado, lanza error 401
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")

    # 🚫 Si cualquier otro error ocurre, lanza error 401
    except:
        raise HTTPException(status_code=401, detail="Token inválido")
    
```

---

### 6. USO EN RUTAS PROTEGIDAS (main.py)

> 🔧 Snippet: mod-auth-protected
> 
1. 📦 Este archivo es el centro de control de tu API
2. 🔓 Activa las rutas públicas (/login, /register)
3. 🔒 Bloquea las rutas privadas (/perfil) si no hay token JWT válido ✅

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


# 🧪 TEST COMPLETO DE REGISTRO, LOGIN Y PERFIL EN FASTAPI

---

### 🔎 Paso 1: Ver qué rutas existen en la API

**Enunciado:**  
Consultar las rutas disponibles que expone FastAPI (usando `openapi.json`)

**Comando terminal:**  
>📍 aText ⇒ :lscurl
```bash
curl -s http://localhost:8000/openapi.json | jq '.paths | keys[]'
```

**Respuesta esperada:**
```
"/"
"/login"
"/perfil"
"/register"
```

**Por qué:**  
Así confirmamos que los endpoints `/login`, `/register` y `/perfil` están correctamente activos en nuestra API.

---

### 🔎 Paso 2: Ver qué datos espera el endpoint `/register` y `/login`

**Enunciado:**  
Consultar la estructura (schema) del cuerpo (`request body`) que esperan los endpoints.

**Comando terminal:**  
>📍 aText ⇒ :curlschema
```bash
curl -s http://localhost:8000/openapi.json | jq '.components.schemas.UserRequest'
```

**Respuesta esperada:**
```json
{
  "properties": {
    "username": { "type": "string", "title": "Username" },
    "password": { "type": "string", "title": "Password" }
  },
  "required": ["username", "password"],
  "title": "UserRequest"
}
```

**Por qué:**  
Así sabes que debes enviar un JSON con `"username"` y `"password"` en el cuerpo de la petición para que funcione correctamente.

---

### 🔎 Paso 3: Registrar un usuario nuevo

**Enunciado:**  
Enviar los datos del usuario a `/register` para guardarlo en la base de datos.

**Comando terminal:**  
>📍 aText ⇒ :curlpost
```bash
curl -X POST http://localhost:8000/register   
-H "Content-Type: application/json"   
-d '{"username": "Jaime", "password": "1111"}'
```

**Respuesta esperada:**
```json
{"message":"✅ Usuario registrado correctamente"}
```

**Por qué:**  
Significa que el usuario `"Jaime"` ya está registrado correctamente en la base de datos y ahora podrá iniciar sesión.

---

### 🔎 Paso 4: Iniciar sesión para obtener el token

**Enunciado:**  
Enviar el usuario y contraseña a `/login` para recibir un token JWT válido.

**Comando terminal:**  
>📍 aText ⇒ :curlpost
```bash
curl -s -X POST http://localhost:8000/login
-H "Content-Type: application/json"   
-d '{"username": "Jaime", "password": "1111"}'
```

**Respuesta esperada (ejemplo):**
```json
{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}
```

**Por qué:**  
Este token sirve como “pase” para acceder a rutas protegidas como `/perfil`. Es como una entrada firmada.

---

### 🔎 Paso 5: Usar el token para acceder al perfil protegido

**Enunciado:**  
Enviar el token como cabecera `Authorization` para entrar al perfil del usuario.

**Comando terminal:**  
>📍 aText ⇒ :curltoken
```bash
curl -s -X GET http://localhost:8000/perfil
-H "Authorization: Bearer TU_TOKEN_AQUI"
```

**Respuesta esperada:**
```json
{"mensaje":"👤 Bienvenido, Jaime"}
```

**Por qué:**  
Significa que el token es válido, que no ha expirado, y que se ha autenticado correctamente al usuario `"Jaime"`.


---

## ✅ CHECKLIST DE COMPRENSIÓN
	•	¿Sabes cómo registrar un usuario y guardar contraseña encriptada?
	•	¿Entiendes cómo se genera un token JWT y cómo se protege una ruta?
	•	¿Puedes añadir Depends(get_current_user) a cualquier endpoint?
	•	¿Has probado con token válido e inválido?

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