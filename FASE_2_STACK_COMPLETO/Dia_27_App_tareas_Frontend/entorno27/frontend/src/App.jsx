// Import básico de React con hooks comunes 📂 ├── src/App.jsx 
// 📍snippet ⇒ react-base-app 
import { useState, useEffect } from "react";
function App() {

// useState para almacenar el array de tareas 📂 ├── src/app.jsx
//📍snippet ⇒ React-estado-tareas
const [tareas, setTareas] = useState([]);

// Estado para input controlado 📂 ├── src/estado/useInput.js
// 📍snippet ⇒ React-estado-input
const [titulo, setTitulo] = useState("");


// useEffect con función de carga(arrowFunction)
//📍snippet ⇒ React-useEffect-load
useEffect(() => {
  // Función fetch para cargar tareas desde FastAPI
  // 📍snippet ⇒ React-fetch-loadTareas
    fetch("http://localhost:8000/tareas")
      .then((res) => res.json())
      .then((data) => setTareas(data));
}, []);

// Función para crear tarea con POST 📂 ├── src/App.jsx
// 📍snippet ⇒ React-crear-tarea-POST
const crearTarea = async (e) => {
  e.preventDefault();
  const nueva = { titulo, done: false };

  const res = await fetch("http://localhost:8000/tareas", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(nueva),
  });

  if (res.ok) {
    const creada = await res.json();
    setTareas([...tareas, creada]);
    setTitulo("");
  }
};

const borrarTarea = async (id) => {
  const res = await fetch(`http://localhost:8000/tareas/${id}`, {
    method: "DELETE",
  });
  if (res.ok) {
    setTareas(tareas.filter((t) => t.id !== id));
  }
};

//Pantalla genérica con formulario e ítems mapeados 📂 ├── src/componentes/Pantalla.jsx
// 📍snippet ⇒ React-pantalla-form-lista-ui
return(
  
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📋 Lista de Tareas</h1>

      <form onSubmit={crearTarea} className="mb-4 flex gap-2">
        <input
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
          placeholder="Escribe algo"
          className="border p-2 w-full rounded"
          required
        />
        <button className="bg-blue-500 text-white px-4 py-2 rounded">
          Añadir
        </button>
      </form>

      <ul className="space-y-2">
        {tareas.map((t) => (
          <li
            key={t.id}
            className={`bg-gray-100 p-2 rounded shadow flex justify-between items-center ${
              t.done ? "line-through text-gray-500" : ""
            }`}
          >
            <span>{t.titulo}</span>
            <button
              onClick={() => borrarTarea(t.id)}
              className="text-red-500 hover:text-red-700"
            >
              🗑️
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}



export default App;