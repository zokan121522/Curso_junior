# 📚 Clase 25 — Conexión Frontend + Backend con Fetch

## 🧠 Objetivo General
Conectar un backend en FastAPI que ofrece tareas vía `/tareas` con un frontend en React que las muestra, usando `fetch()` y `useEffect()`.

---

## 🧱 Estructura Final del Proyecto

```bash
mi-proyecto/
├── backend/
│   ├── main.py               ← API FastAPI (con CORS)
│   ├── tareas.db             ← SQLite con SQLModel
│   ├── env/                  ← Entorno virtual
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   └── App.jsx           ← React (lista de tareas)
│   └── node_modules/
└── README.md
```

---

## 📚 Conceptos Clave

| Concepto       | Explicación técnica | Explicación coloquial                  |
|----------------|---------------------|----------------------------------------|
| **fetch()**     | Llama a una API     | “Ve a buscar los datos al backend”     |
| **useEffect()** | Ejecuta una acción al montar el componente | “Haz esto justo al arrancar” |
| **useState()**  | Guarda datos en memoria | “Memoria interna reactiva”         |
| **map()**       | Recorre listas y genera JSX | “Convierte tareas en elementos visuales” |
| **CORS**        | Permite que el frontend acceda al backend | “Permiso para hablar entre dominios” |
| **FastAPI**     | Framework para crear APIs con Python | “El camarero rápido del backend” |

---

## 🛠 Desarrollo Guiado en 5 Ejercicios

---

### 🔧 Ejercicio 1: Crear el Backend con FastAPI

```bash
# Crear entorno y carpeta
mkdir mi-proyecto && cd mi-proyecto
mkdir backend && cd backend
python3 -m venv env
source env/bin/activate
pip install fastapi uvicorn sqlmodel pydantic
pip freeze > requirements.txt
touch main.py
```

#### Contenido de `main.py`

```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Union

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Tarea(SQLModel, table=True):
    id: Union[int, None] = Field(default=None, primary_key=True)
    titulo: str
    done: bool = False

engine = create_engine("sqlite:///./tareas.db", echo=True)
SQLModel.metadata.create_all(engine)

@app.get("/tareas")
def listar_tareas():
    with Session(engine) as session:
        return session.exec(select(Tarea)).all()
```

---

### 🎨 Ejercicio 2: Crear el Frontend con React

```bash
cd ../
mkdir frontend && cd frontend
# Usa tu script personalizado:
sh ~/scripts/newreact.sh
```

#### App.jsx (usa este snippet)

```jsx
import { useState, useEffect } from "react";

export default function App() {
  const [tareas, setTareas] = useState([]);
  const [cargando, setCargando] = useState(false);

  function loadTareas() {
    setCargando(true);
    fetch("http://localhost:8000/tareas")
      .then((res) => res.json())
      .then((data) => setTareas(data))
      .finally(() => setCargando(false));
  }

  useEffect(() => {
    loadTareas();
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">📋 Lista de Tareas</h1>
      <button
        onClick={loadTareas}
        className="mb-4 px-4 py-2 bg-blue-500 text-white rounded"
      >
        🔁 Refrescar
      </button>
      {cargando ? (
        <p className="text-gray-500">⏳ Cargando tareas...</p>
      ) : (
        <ul className="space-y-2">
          {tareas.map((tarea) => (
            <li
              key={tarea.id}
              className={`p-4 rounded shadow ${tarea.done ? "bg-green-100" : "bg-yellow-100"}`}
            >
              ✅ {tarea.titulo} – {tarea.done ? "Hecho" : "Pendiente"}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

---

### 🔁 Ejercicio 3: Verificar CORS en el backend

Ya está activado con este bloque:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### ⚙️ Ejercicio 4: Uso modular de Snippets

| Snippet Name             | Descripción                           |
|--------------------------|---------------------------------------|
| `react-plantilla-tareas` | Todo el App completo                  |
| `fetch-loadTareas`       | Función sola                          |
| `loader-condicional`     | Loader si está cargando               |
| `boton-refrescar`        | Botón visual bonito                   |
| `li-tarea-color`         | Li que cambia color según `.done`     |

---

### 🔍 Ejercicio 5: Probar todo en local

```bash
# Terminal 1 (backend)
cd backend
source env/bin/activate
uvicorn main:app --reload

# Terminal 2 (frontend)
cd frontend
npm run dev

# Abre navegador:
http://localhost:5173
```

---

## 🔄 Flujo Final

```mermaid
graph LR
  A[React useEffect()] --> B[fetch("/tareas")]
  B --> C[FastAPI GET /tareas]
  C --> D[SQLModel → tareas.db]
  D --> C --> B --> A
```

---

## ✅ Retos Opcionales

- Mostrar total de tareas
- Contar completadas vs pendientes
- Agregar un formulario con POST (próxima clase)
- Mostrar mensaje si no hay tareas

---

📅 Clase generada el 15-08-2025.
