
CRUD básico en FastAPI   

## 📚 Objetivo

## Construir una mini API de tareas con 3 endpoints:
	•	POST /tareas → crear tarea
	•	GET /tareas → listar tareas
	•	DELETE /tareas/{id} → borrar por id

## 🧠 Conceptos nuevos (tabla .md)

| Concepto              | ¿Qué es?                                                                 | ¿Para qué lo usamos aquí? |
|-----------------------|--------------------------------------------------------------------------|---------------------------|
| CRUD                  | 🔄 Significa **Create, Read, Update, Delete** (crear, leer, actualizar, borrar) | Patrón básico de las APIs. Hoy usamos: **crear**, **leer** y **borrar** tareas. |
| SQLModel              | 🛠️ Herramienta que combina **ORM** (manejo de base de datos como objetos) + **Pydantic** (validación de datos) | Definir el modelo **Tarea** y conectar con SQLite. |
| Field                 | 🏷️ Sirve para configurar las columnas de la tabla                        | Indicar **primary_key=True**, valores por defecto, etc. |
| create_engine         | 🔌 Crea la conexión con la base de datos                                 | Abrir conexión a `sqlite:///./tareas.db`. |
| Session               | 📦 "Caja" temporal donde guardamos los cambios antes de confirmarlos     | Añadir, consultar o borrar tareas en la base de datos. |
| select                | 🔍 Orden para consultar datos en SQL                                     | `select(Tarea)` obtiene todas las tareas. |
| @app.post/get/delete  | 🏷️ Decoradores de rutas                                                  | Definen los endpoints de la API para crear, leer y borrar tareas. |
| HTTPException         | 🚨 Forma controlada de enviar errores HTTP                               | Responder con **404** si la tarea no existe. |
| JSONResponse          | 📄 Respuesta en formato JSON personalizada                              | (Opcional) Devolver JSON con código de estado HTTP. |
```
📦 Importaciones principales
|
+-- fastapi
|    |
|    +-- FastAPI           → Crea la aplicación web (servidor)
|    +-- HTTPException     → Lanza errores HTTP controlados
|
+-- fastapi.responses
|    |
|    +-- JSONResponse      → Devuelve respuestas en formato JSON
|
+-- sqlmodel
     |
     +-- SQLModel          → Define modelos/tablas para la base de datos
     +-- Field             → Configura campos (columna, tipo, clave primaria, etc.)
     +-- create_engine     → Conecta con la base de datos (motor SQL)
     +-- Session           → Abre una sesión para leer/escribir datos
     +-- select            → Crea consultas para obtener datos
```
---

## Tabla de importaciones
| Importación | ¿Qué es? | ¿Por qué la necesitamos aquí? |
|-------------|----------|------------------------------|
| `from fastapi import FastAPI` | 🚀 **FastAPI** es el motor que crea y gestiona la API | Nos permite definir rutas como `/tareas` y levantar el servidor. |
| `from fastapi import HTTPException` | 🚨 Herramienta para lanzar errores HTTP controlados | La usamos para devolver un **404** si la tarea no existe. |
| `from fastapi.responses import JSONResponse` | 📄 Permite enviar respuestas personalizadas en formato JSON | La usamos en el **DELETE** para devolver un código `204` sin contenido. |
| `from sqlmodel import SQLModel` | 🛠️ Clase base para definir modelos de base de datos (tablas) y validación de datos | Sirve para crear la tabla **Tarea** y definir sus columnas. |
| `from sqlmodel import Field` | 🏷️ Define opciones de cada columna (clave primaria, valor por defecto…) | Lo usamos para que `id` sea **autoincrement** y `done` tenga valor inicial `False`. |
| `from sqlmodel import create_engine` | 🔌 Crea la conexión con la base de datos | Aquí abre `sqlite:///./tareas.db` para guardar las tareas. |
| `from sqlmodel import Session` | 📦 Es como abrir la caja fuerte de la base de datos 🔓 para meter, sacar o borrar cosas, y luego cerrarla cuando terminas. | Abre, que voy a hacer unos cambios o mirar algo, y luego cierro para que quede todo guardado bien |
| `from sqlmodel import select` | 🔍 Comando para hacer consultas tipo `SELECT * FROM ...` | Lo usamos en el **GET** para traer todas las tareas de la tabla. |
```

┌───────────────┐        ┌────────────┐        ┌────────────┐        ┌──────────────┐
│ Cliente (UI / │  HTTP  │  FastAPI   │  ORM   │  SQLModel  │  Conn  │   SQLite DB  │
│  Postman /    ├────────►  Rutas     ├────────►  Session   ├────────►  tareas.db   │
│  /docs)       │        │ (/tareas)  │        │ (transacc.)│        │ (archivo)    │
└───────────────┘        └────────────┘        └────────────┘        └──────────────┘
        │                         │                     │                      │
        │                         │                     │                      │
        ▼                         ▼                     ▼                      ▼
      (1) POST /tareas
      ───────────────────────────────────────────────────────────────────────────────
      Body JSON: { "titulo": "Aprender FastAPI", "done": false }
          │
          ├─► FastAPI recibe la petición
          │    └─ Valida el JSON contra el modelo `Tarea`
          │
          ├─► Session.add(tarea)
          ├─► Session.commit()        (inserta fila en SQLite)
          ├─► Session.refresh(tarea)  (recupera id autogenerado)
          │
          └─► Respuesta 201 + JSON: { id, titulo, done }

      (2) GET /tareas
      ───────────────────────────────────────────────────────────────────────────────
          │
          ├─► FastAPI entra en la ruta
          ├─► Session.exec(select(Tarea))  (SELECT * FROM tarea)
          ├─► result.all() → lista de tareas
          │
          └─► Respuesta 200 + JSON: [ {id, titulo, done}, ... ]

      (3) DELETE /tareas/{id}
      ───────────────────────────────────────────────────────────────────────────────
          │
          ├─► FastAPI lee {id} de la URL
          ├─► Session.get(Tarea, id)  (busca por PK)
          │     ├─ Si no existe → raise HTTPException(404)
          │     └─ Si existe:
          ├─► Session.delete(tarea)
          ├─► Session.commit()        (borra la fila)
          │
          └─► Respuesta 204 (sin cuerpo)
```

## 📍 Pasos a seguir (API de tareas con 3 endpoints:)
```py
# 📦 1. Importamos FastAPI y SQLModel
# 🚀 2. Instancia de la app
# 🧱 3. Modelo de tabla: Tarea (class)
# 🏎️ 4. Motor SQLite (archivo local)
# 🏗️ 5. Crear tabla: def_()
# ➕ 6. Post / tareas - Crear una tarea 
# 📋 7. Get / tareas - Listar una tarea
# 🗑️ 8. Delete / tareas/{id} - Eliminar una tarea por id
```


## 🧩 Código completo (main.py) — comentado y listo
```py
# 📦 1. Importamos FastAPI y SQLModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel, Field, create_engine, Session, select

# 🚀 2. Instancia de la app
app = FastAPI()

# 🧱 3. Modelo de tabla: Tarea
class Tarea(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True) # 🔑 autoincrement
    titulo: str                   # 🏷️ título de la tarea
    done: bool = False            # ✅ hecha o no (por defecto: False)

# 🏎️ 4. Motor SQLite (archivo local)
engine = create_engine("sqlite:///./tareas.db", echo=True)

# 🏗️ 5. Crear tablas si no existen
def crear_tablas():
    SQLModel.metadata.create_all(engine)

crear_tablas()

# ➕ 6. POST /tareas — Crear una tarea
@app.post("/tareas", status_code=201)
def crear_tarea(tarea: Tarea):
    # Espera JSON: { "titulo": "Aprender FastAPI", "done": false }
    with Session(engine) as session:
        session.add(tarea)       # añade una tarea
        session.commit()         # guarda en DB
        session.refresh(tarea)   # obtiene id autogenerado
        return tarea             # devuelve la tarea creada (con id)

# 📋 7. GET /tareas — Listar todas las tareas
@app.get("/tareas")
def listar_tareas():
    with Session(engine) as session:
        result = session.exec(select(Tarea))  # SELECT * FROM tarea
        return result.all()                   # lista de tareas como JSON

# 🗑️ 8. DELETE /tareas/{id} — Eliminar una tarea por id
@app.delete("/tareas/{id}", status_code=204)
def borrar_tarea(id: int):
    with Session(engine) as session:
        tarea = session.get(Tarea, id)       # Buscar la tarea por su id en BD
        if not tarea:
            # si no existe, devolvemos 404
            raise HTTPException(status_code=404, detail=f"Tarea {id} no encontrada")
        session.delete(tarea)                 # marca para borrar
        session.commit()                      # confirma borrado
        return JSONResponse(content=None, status_code=204)  # sin cuerpo


```
---
## 🚀 Cómo probar rápido
	1.	Arranca el servidor

uvicorn main:app --reload

	2.	Prueba desde la docs (más fácil):

	•	Abre: http://localhost:8000/docs
	•	POST /tareas → “Try it out” → Body:

{ "titulo": "Aprender FastAPI", "done": false }


	•	GET /tareas → verás la lista (incluye id).
	•	DELETE /tareas/{id} → pasa un id existente (p.ej. 1) y ejecuta.

	3.	Postman (si prefieres):

	•	POST http://localhost:8000/tareas → Body raw JSON:

{ "titulo": "Leer docs", "done": false }


	•	GET http://localhost:8000/tareas
	•	DELETE http://localhost:8000/tareas/1

---

## ✅ Mini retos (opcional)
	•	Evitar que se creen tareas sin titulo (valida str no vacío).
	•	Añadir GET /tareas/{id} para obtener una sola tarea.
	•	Añadir PATCH /tareas/{id}/toggle para alternar done (true/false).

### ¡Mini‑retos listos para enchufar! 🔧

>Evitar crear tareas sin título
Opción rápida en la ruta (validación manual):
```py
@app.post("/tareas", status_code=201)
def crear_tarea(tarea: Tarea):
    if not tarea.titulo or not tarea.titulo.strip():
        raise HTTPException(status_code=400, detail="El título no puede estar vacío")
    with Session(engine) as session:
        session.add(tarea)
        session.commit()
        session.refresh(tarea)
        return tarea
```
> (Opcional) Validación en el modelo:
```py
class Tarea(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str = Field(min_length=1)   # 👈 evita cadenas vacías
    done: bool = False
```

> GET /tareas/{id} – obtener una sola tarea
```py
@app.get("/tareas/{id}")
def obtener_tarea(id: int):
    with Session(engine) as session:
        tarea = session.get(Tarea, id)
        if not tarea:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return tarea
```

>PATCH /tareas/{id}/toggle – alternar done
```py
@app.patch("/tareas/{id}/toggle")
def alternar_done(id: int):
    with Session(engine) as session:
        tarea = session.get(Tarea, id)
        if not tarea:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        tarea.done = not tarea.done          # 👈 invierte el estado
        session.add(tarea)
        session.commit()
        session.refresh(tarea)
        return tarea
```
### Prueba rápida en Postman/Docs:
	•	Crear (POST) /tareas con { "titulo": "Comprar pan" }
	•	Obtener una (GET) /tareas/1
	•	Alternar (PATCH) /tareas/1/toggle 👉 done cambia false/true