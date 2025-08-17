# 📂 main.py 🚀 API FastAPI + SQLModel que crea, lista, busca y borra tareas en SQLite con validación de datos.

# 🛠 IMPORTS — Todo lo que necesitamos
from fastapi import FastAPI, HTTPException  # API y errores HTTP
from fastapi.responses import JSONResponse  # Respuesta personalizada
from sqlmodel import SQLModel, Field, create_engine, Session, select
from pydantic import Field as PydField
from typing import Annotated, Union

# ⚙️ INSTANCIA PRINCIPAL DE LA API
app = FastAPI()  # Instancia API

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# 🗄 MODELO PRINCIPAL — Representa la tabla en la BD
class Tarea(SQLModel, table=True):
    id: Union[int, None] = Field(default=None, primary_key=True)
    titulo: str
    done: bool = False

# 📥 MODELO DE ENTRADA — Formato de datos para POST
class TareaCreate(SQLModel):
    titulo: Annotated[str, PydField(min_length=1)]
    done: bool = False

# 🧰 CONFIGURACIÓN BD
engine = create_engine("sqlite:///./tareas.db", echo=True)

def crear_tablas():
    SQLModel.metadata.create_all(engine)

crear_tablas()

# ➕ CREAR TAREA — POST /tareas
@app.post("/tareas", status_code=201)
def crear_tarea(tarea: TareaCreate):
    with Session(engine) as session:
        nueva = Tarea(**tarea.model_dump())
        session.add(nueva)
        session.commit()
        session.refresh(nueva)
        return nueva

# 📜 LISTAR TAREAS — GET /tareas
@app.get("/tareas")
def listar_tareas():
    with Session(engine) as session:
        return session.exec(select(Tarea)).all()

# 🔍 OBTENER TAREA POR ID — GET /tareas/{id}
@app.get("/tareas/{id}")
def obtener_tarea(id: int):
    with Session(engine) as session:
        t = session.get(Tarea, id)
        if not t:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return t

# 🗑 ELIMINAR TAREA — DELETE /tareas/{id}
@app.delete("/tareas/{id}", status_code=204)
def borrar_tarea(id: int):
    with Session(engine) as session:
        t = session.get(Tarea, id)
        if not t:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        session.delete(t)
        session.commit()
        return JSONResponse(content=None, status_code=204)

# ✏️ EDITAR TAREA — PUT /tareas/{id}
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