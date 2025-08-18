
# 🧪 TEST COMPLETO DE REGISTRO, LOGIN Y PERFIL EN FASTAPI

---

### 🔎 Paso 1: Ver qué rutas existen en la API

**Enunciado:**  
Consultar las rutas disponibles que expone FastAPI (usando `openapi.json`)

**Comando terminal:**  
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
```bash
curl -X POST http://localhost:8000/register   -H "Content-Type: application/json"   -d '{"username": "Jaime", "password": "1111"}'
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
```bash
curl -s -X POST http://localhost:8000/login   -H "Content-Type: application/json"   -d '{"username": "Jaime", "password": "1111"}'
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
```bash
curl -s -X GET http://localhost:8000/perfil   -H "Authorization: Bearer TU_TOKEN_AQUI"
```

**Respuesta esperada:**
```json
{"mensaje":"👤 Bienvenido, Jaime"}
```

**Por qué:**  
Significa que el token es válido, que no ha expirado, y que se ha autenticado correctamente al usuario `"Jaime"`.
