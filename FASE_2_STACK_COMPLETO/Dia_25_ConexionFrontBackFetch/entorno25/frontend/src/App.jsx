// 🌐 Componente React para mostrar una lista de elementos desde una API externa
import { useState, useEffect } from "react";

export default function App() {
  // 🔁 Estado para guardar los elementos cargados
  const [items, setItems] = useState([]);

  // ⏳ Estado para mostrar si está cargando
  const [loading, setLoading] = useState(false);

  // 🚀 Función que obtiene datos desde la API
  function loadItems() {
    setLoading(true);
    fetch("http://localhost:8000/tareas") // ← Cambia esta URL por la de tu API
      .then((res) => res.json())
      .then((data) => setItems(data))
      .finally(() => setLoading(false));
  }

  // 📦 Cargar datos automáticamente al montar el componente
  useEffect(() => {
    loadItems();
  }, []);

  // 🖥️ Render de UI
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">📋 Lista de elementos</h1>

      {/* 🔁 Botón para recargar datos manualmente */}
      <button
        onClick={loadItems}
        className="mb-4 px-4 py-2 bg-blue-500 text-white rounded"
      >
        🔁 Refrescar
      </button>

      {/* ⏳ Mostrar cargando o lista */}
      {loading ? (
        <p className="text-gray-500">⏳ Cargando...</p>
      ) : (
        <ul className="space-y-2">
          {items.map((item) => (
            <li
              key={item.id}
              className="p-4 rounded shadow bg-yellow-100"
            >
              <p className="font-semibold">🔸 {item.titulo}</p>
              <p className="text-sm text-gray-600">
                Estado: {item.done ? "Hecho ✅" : "Pendiende ⏳"}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}