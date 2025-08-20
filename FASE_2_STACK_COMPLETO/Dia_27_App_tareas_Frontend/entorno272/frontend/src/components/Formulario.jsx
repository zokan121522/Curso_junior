
import { useState } from "react";

// Estado para input controlado 📂 ├── src/estado/useInput.js
// 📍snippet ⇒ React-estado-input

// Recibo setTareas como prop desde App.jsx para poder actualizar la lista global de tareas desde aquí
export default function Formulario({setTareas}) {

    const [titulo, setTitulo] = useState("");

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
    setTareas((prev) => [...prev, creada]);
    setTitulo("");
  }
};

//Pantalla genérica con formulario e ítems mapeados 📂 ├── src/componentes/Pantalla.jsx
// 📍snippet ⇒ React-pantalla-form-lista-ui
return(

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
  
    );
 }

