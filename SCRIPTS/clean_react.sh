#!/bin/bash

echo "🧹 Limpiando proyecto React con Vite..."

# 1️⃣ Borrar carpeta assets si existe
if [ -d "src/assets" ]; then
  rm -rf src/assets
  echo "✅ Carpeta src/assets eliminada."
fi

# 2️⃣ Borrar App.css si existe
if [ -f "src/App.css" ]; then
  rm src/App.css
  echo "✅ Archivo src/App.css eliminado."
fi

# 3️⃣ Borrar index.css si existe
if [ -f "src/index.css" ]; then
  rm src/index.css
  echo "✅ Archivo src/index.css eliminado."
fi

# 4️⃣ Borrar vite.svg del public si existe
if [ -f "public/vite.svg" ]; then
  rm public/vite.svg
  echo "✅ Archivo public/vite.svg eliminado."
fi

# 5️⃣ Crear carpeta components si no existe
if [ ! -d "src/components" ]; then
  mkdir src/components
  echo "✅ Carpeta src/components creada."
fi

# 6️⃣ Sobrescribir main.jsx limpio
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

# 7️⃣ Sobrescribir App.jsx limpio
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

# 8️⃣ Limpiar README.md
cat <<EOL > README.md
# Mi Proyecto React Limpio

Este proyecto está configurado para empezar desde cero.
React + Vite ⚡

## 🚀 Arranca:
npm install
npm run dev
EOL
echo "✅ README.md limpio generado."

echo "✨ Proyecto minimalista listo para crecer con tus componentes!"