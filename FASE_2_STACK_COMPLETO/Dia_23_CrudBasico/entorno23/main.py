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

# 🗄️ 4. Motor SQLite (archivo local)
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
        session.add(tarea)       # agrega a la transacción
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
