// ✅ 1️⃣ src/components/ContadorPaso.jsx

import { useState } from 'react';

export default function ContadorPaso({ paso }) {
  const [contador, setContador] = useState(0);

  return (
    <div>
      {/* 🔢 Mostrar peldaño actual */}
      <p>Estás en el peldaño: {contador}</p>

      {/* 🔘 Botón: sube la escalera de 'paso' en 'paso' */}
      <button onClick={() => setContador(contador + paso)}>
        Subir +{paso} peldaños
      </button>
    </div>
  );
}