# 📚 CLASE 28 -- App de Tareas: Backend + Base de Datos

## 🧠 OBJETIVO GENERAL

> Aprender a conectar FastAPI con una base de datos real (SQLite) usando
> SQLAlchemy para guardar tareas de forma persistente.

## ⏮️ REQUISITOS PREVIOS

-   Conocer FastAPI (Clase 25)
-   Haber hecho la app de tareas frontend (Clase 27)
-   Tener Python instalado
-   Tener instalado FastAPI + Uvicorn + SQLAlchemy

``` bash
pip install fastapi uvicorn sqlalchemy
```

## 🧩 ¿QUÉ ES CADA COSA?

  --------------------------------------------------------------------------
  Herramienta      ¿Qué hace?
  ---------------- ---------------------------------------------------------
  **SQLite** 🗃️    Una base de datos "de bolsillo", sin servidor. Se guarda
                   como archivo `.db`.

  **SQLAlchemy**   Es un "traductor" entre Python y SQL. Te permite trabajar
  🔗               con tablas sin escribir SQL puro.
  --------------------------------------------------------------------------

## 🎯 METÁFORA SENCILLA

-   FastAPI = Camarero 🧑‍🍳 (recibe pedidos)
-   SQLAlchemy = Traductor 📘 (traduce pedidos a lenguaje de la base de
    datos)
-   SQLite = Almacén 📦 (guarda los platos ya servidos)

## 1. 🏗️ ESTRUCTURA DEL PROYECTO

    📁 backend/
     ├── main.py            # Donde vive FastAPI
     ├── database.py        # Configuración de la base de datos
     ├── models.py          # Tablas de la base de datos
     ├── schemas.py         # Validación de datos (entrada/salida)
     └── crud.py            # Funciones para operar con la DB

## 2. 🧱 CREAR LOS ARCHIVOS BASE

### `database.py`

``` python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./tareas.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### `models.py`

``` python
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    done = Column(Boolean, default=False)
```

### `schemas.py`

``` python
from pydantic import BaseModel

class TareaBase(BaseModel):
    titulo: str

class TareaCrear(TareaBase):
    pass

class Tarea(TareaBase):
    id: int
    done: bool

    class Config:
        orm_mode = True
```

### `crud.py`

``` python
from sqlalchemy.orm import Session
from . import models, schemas

def get_tareas(db: Session):
    return db.query(models.Tarea).all()

def crear_tarea(db: Session, tarea: schemas.TareaCrear):
    nueva = models.Tarea(titulo=tarea.titulo)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def borrar_tarea(db: Session, id: int):
    tarea = db.query(models.Tarea).get(id)
    if tarea:
        db.delete(tarea)
        db.commit()
    return tarea

def toggle_tarea(db: Session, id: int, estado: bool):
    tarea = db.query(models.Tarea).get(id)
    if tarea:
        tarea.done = not estado
        db.commit()
        db.refresh(tarea)
    return tarea
```

## 3. 🚀 `main.py`

``` python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tareas", response_model=list[schemas.Tarea])
def leer_tareas(db: Session = Depends(get_db)):
    return crud.get_tareas(db)

@app.post("/tareas", response_model=schemas.Tarea)
def nueva_tarea(tarea: schemas.TareaCrear, db: Session = Depends(get_db)):
    return crud.crear_tarea(db, tarea)

@app.delete("/tareas/{id}")
def borrar(id: int, db: Session = Depends(get_db)):
    return crud.borrar_tarea(db, id)

@app.put("/tareas/{id}", response_model=schemas.Tarea)
def toggle(id: int, db: Session = Depends(get_db)):
    tarea_actual = db.query(models.Tarea).get(id)
    return crud.toggle_tarea(db, id, tarea_actual.done)
```

## 🧪 PRUEBA LA API

``` bash
uvicorn main:app --reload
```

Visita <http://localhost:8000/docs>

## ✅ CHECKLIST

  Concepto                     Entendido ✅
  ---------------------------- --------------
  - [ ] Crear base de datos SQLite   
  - [ ] Usar SQLAlchemy como ORM     
  - [ ] Crear modelos y esquemas     
  - [ ] Enlazar FastAPI con DB       
  - [ ] Probar con Swagger           

## 💪 EJERCICIOS

- [ ] 1.  Crea una tarea desde el frontend y comprueba que se guarda.
- [ ] 2.  Marca como hecha desde el frontend y revisa el campo `done` en
    Swagger.
- [ ] 3.  Borra una tarea desde el frontend y revisa si desaparece de la base
    de datos.
