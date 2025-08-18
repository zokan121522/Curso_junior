# Crear tablas SQLModel desde modelo y engine externo 📂 ├──create_db.py
# 📍 snipet ⇒ init-db-sqlmodel-createdb
from sqlmodel import SQLModel
from models import User
from database import engine

SQLModel.metadata.create_all(engine)
print("✅ Base de datos y tabla User creada correctamente")