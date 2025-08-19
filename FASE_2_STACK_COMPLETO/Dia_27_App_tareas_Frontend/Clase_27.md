# Clase 27 – App de tareas (Frontend).
En esta clase crearemos el cliente web de la API que ya tienes lista. Usaremos React para:

---

## 🧠 OBJETIVO GENERAL

#### Crear una interfaz React funcional que permita:
	•	Ver tareas desde la API.
	•	Crear nuevas tareas con un formulario.
	•	Ver la lista actualizada dinámicamente (sin recargar).

---

## ️ REQUISITOS PREVIOS
```
  1.	Tener corriendo el backend (main.py) 
  2.  📌 ENDPOINTS ⇒ obtener, crear, listar , eliminar , editar
  3.  Probar api con curl (TABLA)
  3.	API funcionando en http://localhost:8000
  4. 	Proyecto React creado (con Vite y Tailwind si quieres estilo rápido)
``` 
> Ver clase dia_25
# 🧪 Pruebas de API FastAPI con curl

| Método | Endpoint             | Código curl                                                                                           | Respuesta esperada                           |
|--------|----------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------|
| POST   | /tareas              | curl -X POST http://localhost:8000/tareas \ <br> -H "Content-Type: application/json" \ <br> -d '{"titulo": "Aprender FastAPI", "done": false}' | { "id": 1, "titulo": "Aprender FastAPI", "done": false } |
| GET    | /tareas              | curl http://localhost:8000/tareas                                                                       | [ { "id": 1, "titulo": "Aprender FastAPI", "done": false } ] |
| GET    | /tareas/1            | curl http://localhost:8000/tareas/1                                                                     | { "id": 1, "titulo": "Aprender FastAPI", "done": false } |
| PUT    | /tareas/1            | curl -X PUT http://localhost:8000/tareas/1 \ <br> -H "Content-Type: application/json" \ <br> -d '{"titulo": "FastAPI actualizado", "done": true}' | { "id": 1, "titulo": "FastAPI actualizado", "done": true } |
| DELETE | /tareas/1            | curl -X DELETE http://localhost:8000/tareas/1                                                           | (No content) → status 204                    |
| GET    | /tareas/1 (borrado)  | curl http://localhost:8000/tareas/1                                                                     | { "detail": "Tarea no encontrada" }          |
---

## 1. 🏗️ ESTRUCTURA BÁSICA DEL PROYECTO FRONTEND
> Con la script esta podresmos crear un proyecto en segundos ⇒ ./newreact.sh frontend
```bash
# Lo podemos hacer manualmente tambien.

npm create vite@latest tareas-front -- --template react
cd tareas-front
npm install
npm run dev

# Instala TailwindCSS (opcional pero recomendado para estilos rápidos):

npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Y añade en tailwind.config.js:

content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"]

# Y en src/index.css:

@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## 2. 📄 CREAR COMPONENTE <App /> Y ESTRUCTURA BÁSICA

#### MONTAR App.jsx SOLO CON TUS SNIPPETS

| 🧩 BLOQUE                         | ✅ SNIPPET A USAR             | 📂 Ruta dentro del proyecto              | ✅ Completado |
|----------------------------------|-------------------------------|------------------------------------------|---------------|
| `import { useEffect, useState }` | `react-base`                  | 📂 ├── src/App.jsx                        | - [x]         |
| `const [tareas, setTareas]`      | `estado-tareas-react`         | 📂 ├── src/App.jsx                        | - [x]         |
| `const [titulo, setTitulo]`      | `estado-input`                | 📂 ├── src/App.jsx                        | - [x]         |
| `useEffect(() => loadTareas())`  | `useEffect-load`              | 📂 ├── src/App.jsx                        | - [ ]         |
| Función `loadTareas()`           | `fetch-loadTareas`            | 📂 ├── src/funciones/loadTareas.js        | - [ ]         |
| Función `crearTarea` (POST)      | a) `crear-tarea`              | 📂 ├── src/funciones/crearTarea.js        | - [ ]         |
|                                  | b) `crear-Tarea-POST-react`   | 📂 ├── src/App.jsx                        | - [ ]         |
| Formulario                       | `form-tarea`                  | 📂 ├── src/componentes/FormTarea.jsx      | - [ ]         |
| Lista tareas `.map()`            | `map-tareas-ui`               | 📂 ├── src/componentes/ListaTareas.jsx    | - [ ]         |
---

```jsx
// src/App.jsx
import { useEffect, useState } from "react";

function App() {
  const [tareas, setTareas] = useState([]);
  const [titulo, setTitulo] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/tareas")
      .then(res => res.json())
      .then(data => setTareas(data));
  }, []);

  const crearTarea = async (e) => {
    e.preventDefault();
    const nueva = { titulo, done: false };

    const res = await fetch("http://localhost:8000/tareas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(nueva),
    });

    if (res.ok) {
      const tareaCreada = await res.json();
      setTareas([...tareas, tareaCreada]);
      setTitulo("");
    }
  };

  return (
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📋 Lista de Tareas</h1>

      <form onSubmit={crearTarea} className="mb-4 flex gap-2">
        <input
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
          placeholder="Nueva tarea"
          className="border p-2 w-full rounded"
          required
        />
        <button className="bg-blue-500 text-white px-4 py-2 rounded">Añadir</button>
      </form>

      <ul className="space-y-2">
        {tareas.map((t) => (
          <li key={t.id} className="bg-gray-100 p-2 rounded shadow">
            {t.titulo}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

---

## 3. 🧠 Tabla de conceptos - App de Tareas (Frontend)

| 🔧 Concepto                  | 📘 ¿Qué es técnicamente?                                                                 | 🧠 ¿Cómo lo entiendes tú?                                                                 |
|-----------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 🎯 `useState`               | Hook de React para guardar valores y actualizarlos dinámicamente.                       | 🧺 Como una caja mágica donde guardas datos que pueden cambiar.                          |
| ⚡ `useEffect`              | Hook que se ejecuta al cargar el componente o cuando cambia algo.                       | 🚪 Como poner una alarma que suena al abrir la puerta (ejecutar código al cargar).       |
| 🌍 `fetch()`                | Función para hacer peticiones HTTP al backend (GET, POST...).                           | 📬 Manda un sobre con info al servidor y espera su respuesta.                            |
| 📝 `onSubmit`              | Evento que salta al enviar un formulario.                                               | 🚀 Lanza la acción de "añadir tarea" cuando pulsas el botón.                             |
| ❌ `e.preventDefault()`     | Evita que el formulario recargue la web al enviarse.                                   | 🚫 Le dices al navegador: “tranquilo, no recargues, yo me encargo”.                      |
| 🧾 `JSON.stringify()`       | Convierte un objeto JavaScript en texto JSON para enviarlo al servidor.                 | ✉️ Convierte tu carta en formato “comprensible” para el backend.                        |
| 🧩 `setTareas([...])`       | Actualiza el estado agregando una tarea a la lista anterior sin borrarla.               | 🧃 Añades una nueva tarea a la lista sin tirar las anteriores.                           |
| 🔄 `.map()`                 | Recorre arrays y transforma cada elemento (para pintar listas).                         | 🖼️ Convierte datos en elementos visuales como tarjetas o párrafos.                      |
| ✍️ `value` + `onChange`     | Controlan lo que escribes en un input (formulario controlado).                         | 🧠 React se entera de cada letra que escribes para guardar el texto.                     |
| ⏳ `async` / `await`        | Manejan código asíncrono como peticiones a la API sin bloquear la app.                 | 🛎️ Pides una tarea, te sientas tranquilo hasta que llegue sin congelar todo lo demás.    |

---

## 4. ✅ CHECKLIST DE APRENDIZAJE
	•	Saber cómo usar fetch en React
	•	Comprender useState y useEffect
	•	Enviar datos al backend con POST
	•	Actualizar el DOM dinámicamente

---

## 5. 💪 EJERCICIOS PROPUESTOS
	1.	Cambia el diseño para que las tareas tachadas se vean en gris.
	2.	Añade un botón para borrar tareas.
	3.	Marca una tarea como hecha (requiere un PUT).
	4.	Ordena tareas por fecha o estado.

---
