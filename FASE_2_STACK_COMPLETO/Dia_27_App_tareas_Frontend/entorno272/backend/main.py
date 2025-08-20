# 🚀 API base FastAPI + SQLModel conectada a SQLite, lista para endpoints CRUD  📂 ├──  main.py  
# 📍snippet ⇒ FastApi-template-sql-app
# 🛠 IMPORTS — Librerías necesarias
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Field, create_engine, Session, select
from pydantic import Field as PydField
from typing import Annotated, Union
# ⚙️ APP — Crear instancia de la API
app = FastAPI()
# 🌐 Middleware CORS — Permitir conexión desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 🗄 MODELO PRINCIPAL — Tarea (para la base de datos)
class Tarea(SQLModel, table=True):
    id: Union[int, None] = Field(default=None, primary_key=True)
    titulo: str
    done: bool = False
# 📝 MODELO DE ENTRADA — Para crear/editar tareas
class TareaCreate(SQLModel):
    titulo: Annotated[str, PydField(min_length=1)]
    done: bool = False
# 🔌 BASE DE DATOS — Configuración SQLite
engine = create_engine("sqlite:///./tareas.db", echo=True)
def crear_tablas():
    SQLModel.metadata.create_all(engine)
crear_tablas()
# 📌 ENDPOINTS — Agrégalos debajo

# 📜 LISTAR TAREAS — GET /tareas ⇒ 📂 ├── main.py
# 📍snippet ⇒ Fastapi-endpoint-get-listar
@app.get("/tareas")
def listar_tareas():
    with Session(engine) as session:
        return session.exec(select(Tarea)).all()

# 🔍 OBTENER TAREA POR ID — GET /tareas/{id} ⇒ 📂 ├── main.py
# 📍snippet ⇒ FastApi-endpoint-getID-listarId
@app.get("/tareas/{id}")
def obtener_tarea(id: int):
    with Session(engine) as session:
        t = session.get(Tarea, id)
        if not t:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return t
    
# ✏️ EDITAR TAREA — PUT /tareas/{id} ⇒ 📂 ├── main.py
# 📍snippet ⇒ FastApi-endpoint-edit-put-editarTarea
@app.put("/tareas/{id}")
def editar_tarea(id: int, tarea: TareaCreate):
    with Session(engine) as session:
        existente = session.get(Tarea, id)  # 🔍 Buscar tarea por ID
        if not existente:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        existente.titulo = tarea.titulo       # 📝 Actualizar título
        existente.done = tarea.done           # ✅ Actualizar estado
        session.add(existente)                # 💾 Guardar cambios
        session.commit()
        session.refresh(existente)
        return existente
# 🗑 ELIMINAR TAREA — DELETE /tareas/{id} ⇒ 📂 ├── main.py
# 📍snippet ⇒ FastApi-endpoint-delete-borrarId
@app.delete("/tareas/{id}", status_code=204)
def borrar_tarea(id: int):
    with Session(engine) as session:
        t = session.get(Tarea, id)
        if not t:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        session.delete(t)
        session.commit()
        return JSONResponse(content=None, status_code=204)
    
# ➕ CREAR TAREA — POST /tareas ⇒ 📂 ├── main.py
# 📍snippet ⇒ FastApi-endpoint-post
@app.post("/tareas", status_code=201)
def crear_tarea(tarea: TareaCreate):
    with Session(engine) as session:
        nueva = Tarea(**tarea.model_dump())
        session.add(nueva)
        session.commit()
        session.refresh(nueva)
        return nueva
    
