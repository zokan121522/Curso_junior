
# 🧪 Ejercicios Propuestos – App de Tareas

Perfecto, vamos a resolver los 4 ejercicios que has propuesto sobre tu app de tareas. Los haré uno a uno, explicando paso a paso qué cambia, por qué y dónde, y luego te doy el código exacto para que lo puedas copiar o convertir en snippet.

---

## ✅ EJERCICIO 1: Cambiar diseño para que las tareas tachadas se vean en gris

### 🎯 Objetivo:
Visualmente distinguir las tareas completadas (`done: true`) con texto tachado y color gris.

### 🧠 ¿Qué debes hacer?
1. Cambiar el mapeo de la lista (`tareas.map`) para comprobar `t.done`.
2. Aplicar clases condicionales de Tailwind según el estado.

### 💡 Paso a paso:
```jsx
<ul className="space-y-2">
  {tareas.map((t) => (
    <li
      key={t.id}
      className={`bg-gray-100 p-2 rounded shadow ${t.done ? "line-through text-gray-500" : ""}`}
    >
      {t.titulo}
    </li>
  ))}
</ul>
```

### 📌 Explicación:
- `t.done ? "line-through text-gray-500"`: si la tarea está marcada como hecha, añade esas clases de Tailwind.
- `line-through`: tachado.
- `text-gray-500`: color gris claro.

---

## ✅ EJERCICIO 2: Añadir un botón para borrar tareas

### 🎯 Objetivo:
Permitir al usuario eliminar tareas usando un botón junto a cada ítem.

### 🧠 ¿Qué debes hacer?
1. Crear una función `borrarTarea(id)` con `fetch DELETE`.
2. Añadir un botón en cada `<li>`.

### 💡 Paso a paso:
```js
const borrarTarea = async (id) => {
  const res = await fetch(`http://localhost:8000/tareas/${id}`, {
    method: "DELETE",
  });
  if (res.ok) {
    setTareas(tareas.filter((t) => t.id !== id));
  }
};
```

```jsx
<ul className="space-y-2">
  {tareas.map((t) => (
    <li
      key={t.id}
      className={`bg-gray-100 p-2 rounded shadow flex justify-between items-center ${t.done ? "line-through text-gray-500" : ""}`}
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
```

---

## ✅ EJERCICIO 3: Marcar una tarea como hecha (requiere PUT)

### 🎯 Objetivo:
Cambiar el estado de `done: false` a `true` y viceversa con un clic.

### 🧠 ¿Qué debes hacer?
1. Crear función `toggleTarea(id, done)` → hace PUT a la API.
2. Añadir un botón o `span` clickable.

### 💡 Paso a paso:
```js
const toggleTarea = async (id, done) => {
  const res = await fetch(`http://localhost:8000/tareas/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ done: !done }),
  });

  if (res.ok) {
    const actualizada = await res.json();
    setTareas(tareas.map((t) => (t.id === id ? actualizada : t)));
  }
};
```

```jsx
<span
  onClick={() => toggleTarea(t.id, t.done)}
  className="cursor-pointer flex-1"
>
  {t.titulo}
</span>
```

---

## ✅ EJERCICIO 4: Ordenar tareas por fecha o estado

### 🎯 Objetivo:
Mostrar tareas según una lógica: por ejemplo, hechas al final.

### 🧠 ¿Qué debes hacer?
1. Ordenar el array `tareas` antes de mostrarlo.
2. Ejemplo: primero tareas pendientes, luego hechas.

### 💡 Paso a paso:
```js
const tareasOrdenadas = [...tareas].sort((a, b) => {
  return Number(a.done) - Number(b.done); // false (0) va antes que true (1)
});
```

```jsx
{tareasOrdenadas.map(...)}
```

---

## 🧩 BONUS: Snippet genérico para tarea completa con toggle y delete

```jsx
// 📍snippet ⇒ React-lista-tareas-avanzada
<ul className="space-y-2">
  {${1:items}.map((item) => (
    <li
      key={item.id}
      className={`p-2 rounded shadow flex justify-between items-center ${
        item.done ? "line-through text-gray-500 bg-gray-50" : "bg-white"
      }`}
    >
      <span
        onClick={() => ${2:toggleDone}(item.id, item.done)}
        className="cursor-pointer flex-1"
      >
        {item.titulo}
      </span>
      <button
        onClick={() => ${3:borrarItem}(item.id)}
        className="text-red-500 hover:text-red-700"
      >
        🗑️
      </button>
    </li>
  ))}
</ul>
```

---

¿Quieres que prepare esta versión como módulo por separado (`ListaTareasAvanzada.jsx`) y sus funciones (`borrarTarea.js`, `toggleTarea.js`) también?
