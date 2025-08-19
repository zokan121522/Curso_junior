// Import básico de React con hooks comunes 📂 ├── src/App.jsx 
// 📍snippet ⇒ react-base 
import { useState, useEffect } from "react";
function App() {

  // useState para almacenar el array de tareas 📂 ├── src/app.jsx
  //📍snippet ⇒ estado-tareas-react
  const [tareas, setTareas] = useState([]);

  // Estado para input controlado 📂 ├── src/estado/useInput.js
  // 📍snippet ⇒ estado-input
  const [titulo, setTitulo] = useState("");

  // useEffect con función de carga(arrowFunction)
  //📍snippet ⇒ useEffect-load-react
  useEffect(() => {
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

//Pantalla genérica con formulario e ítems mapeados 📂 ├── src/componentes/Pantalla.jsx
// 📍snippet ⇒ React-pantalla-form-lista-ui
<div className="p-8 max-w-xl mx-auto">
  <h1 className="text-2xl font-bold mb-4">📋 Lista de tareas</h1>

  <form onSubmit={crearTarea} className="mb-4 flex gap-2">
    <input
      value={titulo}
      onChange={(e) => setTitulo(e.target.value)}
      placeholder="Nueva Tarea"
      className="border p-2 w-full rounded"
      required
    />
    <button className="bg-blue-500 text-white px-4 py-2 rounded">
      Añadir
    </button>
  </form>

  <ul className="space-y-2">
    {tareas.map((t) => (
      <li key={t.id} className="bg-gray-100 p-2 rounded shadow">
        {t.titulo}
      </li>
    ))}
  </ul>
</div>

}

export default App