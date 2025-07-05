#!/bin/bash

echo "🧹 Limpiando proyecto React con Vite..."

# Borrar carpeta assets si existe
if [ -d "src/assets" ]; then
  rm -rf src/assets
  echo "✅ Carpeta src/assets eliminada."
fi

# Crear carpeta components si no existe
if [ ! -d "src/components" ]; then
  mkdir src/components
  echo "✅ Carpeta src/components creada."
fi

# Sobrescribir main.jsx limpio
cat <<EOL > src/main.jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
EOL

echo "✅ main.jsx limpio generado."

# Sobrescribir App.jsx limpio
cat <<EOL > src/App.jsx
export default function App() {
  return (
    <div>
      <h1>Mi App React Limpia 🚀</h1>
      {/* Aquí irán tus componentes */}
    </div>
  )
}
EOL

echo "✅ App.jsx limpio generado."

echo "✨ Proyecto limpio y listo para tus componentes!"