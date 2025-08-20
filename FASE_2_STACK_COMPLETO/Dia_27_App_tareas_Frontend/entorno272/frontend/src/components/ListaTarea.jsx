// Componente genérico con botón para eliminar items de una lista
// 📍snippet ⇒ React-Lista-eliminar-borrar-ConBotonEliminar
export default function ListaTarea({ tareas, setTareas }) {
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