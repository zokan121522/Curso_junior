# 📍 snippet ⇒ sqlite-engine-database
# Snippet para crear motor SQLite con SQLModel 📂 ├── database.py
from sqlmodel import create_engine

engine = create_engine("sqlite:///db.db", echo=True)