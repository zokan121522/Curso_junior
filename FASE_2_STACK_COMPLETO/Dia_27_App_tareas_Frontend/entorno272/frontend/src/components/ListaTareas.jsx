// 📍snippet ⇒ React-lista-tareas-toggle-delete 📂 ├── src/components/ListaTareas.jsx
export default function ListaTareas({ tareas, setTareas }) {

  // ✅ 1. Toggle: marcar como hecha o deshecha (PUT)
  const toggleTarea = async (id, done, titulo) => {
    const res = await fetch(`http://localhost:8000/tareas/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ titulo, done: !done }),
    });

    if (res.ok) {
      const actualizada = await res.json();
      setTareas((prev) =>
        prev.map((t) => (t.id === id ? actualizada : t))
      );
    }
  };

  // 🗑️ 2. Borrar tarea (DELETE)
  const borrarTarea = async (id) => {
    const res = await fetch(`http://localhost:8000/tareas/${id}`, {
      method: "DELETE",
    });
    if (res.ok) {
      setTareas((prev) => prev.filter((t) => t.id !== id));
    }
  };

  // 🧠 3. Ordenar tareas: pendientes arriba, hechas abajo
  const tareasOrdenadas = [...tareas].sort((a, b) => Number(a.done) - Number(b.done));

  return (
    <ul className="space-y-2">
      {tareasOrdenadas.map((t) => (
        <li
          key={t.id}
          className={`p-2 rounded shadow flex justify-between items-center ${t.done ? "line-through text-gray-500 bg-gray-50" : "bg-white"}`}
        >
          <span
            onClick={() => toggleTarea(t.id, t.done, t.titulo)}
            className="cursor-pointer flex-1"
          >
            {t.titulo} {t.done ? " hecho ✅" : " pendiente⏳"}
          </span>
          <button
            onClick={() => borrarTarea(t.id)}
            className="text-red-500 hover:text-red-700 ml-2"
          >
            🗑️
          </button>
        </li>
      ))}
    </ul>
  );
}