// ✅ Exportamos nuestro componente ListaNombres
export default function ListaNombres({ nombres }) { 
  // 🔑 Recibe 'nombres' como prop → es como recibir una caja de nombres

  return (
    <div>
      {/* 🔄 Usamos map para recorrer cada nombre de la lista */}
      {nombres.map((nombre, index) => ( 
        // 🧩 Por cada nombre, devuelve un bloque con clave única 'key'
        <div key={index}>
          {/* 🎟️ key={index} → identifica cada elemento para que React no se confunda */}

          {/* 👤 Muestra el nombre */}
          <span>{nombre}</span>

          {/* 👋 Botón para saludar (no hace nada aún) */}
          <button>Saludar</button>
        </div>
      ))}
    </div>
  );
}

// ✅ Recibe datos como prop               🗃️ Caja de datos (prop)
// ✅ Usa map() para recorrer              ➡️ map() = cinta transportadora
// ✅ Devuelve JSX por cada ítem
// ✅ Pon key única                        🔑 key = número de serie
// ✅ Muestra el dato dentro del JSX       🎨 JSX = molde de salida

