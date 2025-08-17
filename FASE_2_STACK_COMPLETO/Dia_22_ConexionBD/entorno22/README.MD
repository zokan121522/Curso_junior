# 📦 API de Usuarios con FastAPI + SQLite

Este proyecto es una API básica construida con **FastAPI** y **SQLModel**, que permite guardar y consultar usuarios en una base de datos **SQLite** local.

---

## 🚀 Funcionalidades

- **POST /usuarios** → Crea un nuevo usuario (requiere `nombre` y `edad`)
- **GET /usuarios** → Lista todos los usuarios registrados

---

## 📂 Estructura del Proyecto

```bash
.
├── main.py               # Código principal de la API
├── usuarios.db           # Base de datos SQLite (se crea al ejecutar)
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```