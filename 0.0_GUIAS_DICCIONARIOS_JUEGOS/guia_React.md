¡Aquí tienes la versión resumida en formato .md solo con los primeros pasos para arrancar un proyecto React con Vite!

# 🚀 Guía Express
# Crear Proyecto React con Vite y Limpiar con script clean_react.sh

## ✅ 1. Crear proyecto

```bash
npm create vite@latest mi-proyecto-react -- --template react
cd mi-proyecto-react
npm install
npm run dev
```
	•	npm create vite@latest ... → Genera la estructura base.
	•	cd mi-proyecto-react → Entras en tu carpeta.
	•	npm install → Instala dependencias.
	•	npm run dev → Levanta servidor local → http://localhost:5173
---

## ✅ 2. Estructura básica
```bash
/src
 ├── App.jsx     # Componente principal
 ├── main.jsx    # Entrada React
 └── components/ # 🧩 Aquí pondrás tus piezas
```

---

## ✅ 3. Ver en navegador
```bash
	•	Abre http://localhost:5173
	•	Verás la plantilla de Vite + React funcionando.
	•	Edita App.jsx para ver el hot reload en acción.
```
---
## ✅ 4. Limpiar proyecto con : 
```bash
 ~/scripts/clean_react.sh 
```
> Desde la ruta del proyecto en sí, ejecuta esta script.

## 📌 Tip:
```bash
Piensa en cada componente como un bloque Lego 🧩.
Crea piezas pequeñas → luego encájalas.
```