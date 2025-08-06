#!/bin/bash

# newreact.sh
# 🚀 Generador de boilerplate React + Vite + TailwindCSS 3.4.3 con card funcional

APP_NAME=$1

if [ -z "$APP_NAME" ]; then
  echo "❌ Debes escribir un nombre para tu app: ./newreact.sh mi-proyecto"
  exit 1
fi

echo "🚧 Creando proyecto: $APP_NAME"

npm create vite@latest "$APP_NAME" -- --template react
cd "$APP_NAME" || exit

echo "📦 Instalando dependencias..."
npm install
npm install -D tailwindcss@^3.4.3 postcss autoprefixer
npx tailwindcss init -p

echo "⚙️ Configurando TailwindCSS..."
cat > tailwind.config.js <<EOF
export default {
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOF

cat > postcss.config.js <<EOF
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
EOF

echo "🎨 Creando index.css con Tailwind..."
cat > src/index.css <<EOF
@tailwind base;
@tailwind components;
@tailwind utilities;
EOF

echo "🔧 Generando main.jsx y App.jsx..."
cat > src/main.jsx <<EOF
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
EOF

cat > src/App.jsx <<EOF
import Card from './components/Card'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center p-6">
      <Card />
    </div>
  )
}
EOF

echo "🧩 Creando componente Card..."
mkdir -p src/components
cat > src/components/Card.jsx <<EOF
export default function Card() {
  return (
    <div className="bg-white shadow-2xl rounded-2xl overflow-hidden max-w-sm transition hover:scale-105 hover:shadow-black/30 duration-300">
      <img
        src="https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?auto=format&fit=crop&w=800&q=80"
        alt="Imagen segura"
        className="w-full h-48 object-cover"
      />
      <div className="p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">Título de la tarjeta</h2>
        <p className="text-gray-600 mb-4">
          Esta es una descripción de ejemplo. Puedes personalizarla como quieras para destacar tu contenido.
        </p>
        <button className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white px-4 py-2 rounded-lg font-medium transition-all">
          Ver más
        </button>
      </div>
    </div>
  )
}
EOF

echo "📂 Añadiendo .gitignore"
cat > .gitignore <<EOF
node_modules
dist
.env
EOF

echo "✅ Proyecto '$APP_NAME' creado correctamente con Tailwind 3.4.3"
echo ""
echo "👉 Para empezar:"
echo "cd $APP_NAME"
echo "npm run dev"