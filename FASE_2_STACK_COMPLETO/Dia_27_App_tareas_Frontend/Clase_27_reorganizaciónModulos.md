
# 📦 Modularización del Proyecto React de Lista de Tareas

Perfecto. Vamos a modularizar tu proyecto en componentes, usando solo los snippets que ya tienes definidos, y asegurándonos de que cada constante esté definida en su propio componente cuando sea posible.

---

## ✅ OBJETIVO:
1. Modularizar tu app en componentes.
2. Indicar qué snippet usar en cada uno.
3. Ver si es viable definir el estado y funciones dentro de cada componente.

---

## 🧩 COMPONENTES PROPUESTOS

| Componente         | ¿Qué hace?                 | Snippet base                             | ¿Define constantes internas? |
|--------------------|----------------------------|------------------------------------------|-------------------------------|
| `App.jsx`          | Orquesta todo. Pasa props. | `react-base-app`                         | ✅ Define `tareas`, `setTareas` |
| `Formulario.jsx`   | Input + botón              | `React-pantalla-form-lista-ui` (adaptado) | ✅ Define `titulo`, `setTitulo` |
| `ListaTareas.jsx`  | Renderiza lista de tareas  | `map-tareas-ui` o `React-lista-tareas-avanzada` | ❌ Usa `tareas` como prop |
| `useInput.js` (opcional) | Hook para input       | `React-estado-input`                     | ✅ (si quieres externalizar input) |

---

## 🧱 REORGANIZACIÓN FINAL (CON SNIPPETS)

### 📂 src/App.jsx

##### 🧠 Snippets usados en `App.jsx` (explicación clara y visual)

| 🧩 Snippet                  | 🔍 ¿Qué hace?                                                                 |
|----------------------------|------------------------------------------------------------------------------|
| `react-base-app`           | Estructura básica de un componente con `useState` y `useEffect`.            |
| `React-estado-tareas`      | Declara el estado `tareas` y su modificador `setTareas`.                    |
| `React-useEffect-load`     | Define un `useEffect` que se ejecuta al cargar el componente.               |
| `React-fetch-loadTareas`   | Dentro del `useEffect`, hace un fetch a la API para obtener las tareas.     |


```jsx
import { useEffect, useState } from "react";
import Formulario from "./components/Formulario";
import ListaTareas from "./components/ListaTareas";

function App() {
  const [tareas, setTareas] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/tareas")
      .then((res) => res.json())
      .then((data) => setTareas(data));
  }, []);

  return (
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📋 Lista de Tareas</h1>
      <Formulario setTareas={setTareas} />
      <ListaTareas tareas={tareas} setTareas={setTareas} />
    </div>
  );
}

export default App;
```

---

### 📂 src/components/Formulario.jsx

**Snippets usados:**
- `estado-input`
- `React-crear-tarea-POST`

```jsx
import { useState } from "react";

export default function Formulario({ setTareas }) {
  const [titulo, setTitulo] = useState("");

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

  return (
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
```

---

### 📂 src/components/ListaTareas.jsx

**Snippets usados:**
- `map-tareas-ui`
- `React-lista-tareas-avanzada`

```jsx
// Componente genérico con botón para eliminar items de una lista
// 📍snippet ⇒ React-Lista-eliminar-borrar-ConBotonEliminar
export default function ListaTareas({ tareas, setTareas }) {
  const borrar = async (id) => {
    const res = await fetch(`http://localhost:8000/items/id`, {
      method: "DELETE",
    });
    if (res.ok) {
      setTareas((prev) => prev.filter((item) => item.id !== id));
    }
  };

  return (
    <ul>
      {tareas.map((tarea) => (
        <li key={tarea.id}>
          {tareas.nombre}
          <button onClick={() => borrar(tarea.id)}>🗑️</button>
        </li>
      ))}
    </ul>
  );
}
```

---

## ✅ CONCLUSIÓN: ¿Dónde definir las constantes?

| Constante          | ¿Dónde va?        | ¿Por qué?                                        |
|--------------------|-------------------|--------------------------------------------------|
| `tareas`, `setTareas` | App.jsx         | Porque es el estado global que se comparte.      |
| `titulo`, `setTitulo` | Formulario.jsx  | Solo lo usa ese componente.                      |
| `crearTarea()`     | Formulario.jsx    | Solo se usa al hacer submit del formulario.      |
| `borrarTarea()`    | ListaTareas.jsx   | Solo lo necesita el listado para borrar.         |
