// Import básico de React con hooks comunes 📂 ├── src/App.jsx 
// 📍snippet ⇒ react-base-app 
import { useState, useEffect } from "react";
import Formulario from "./components/Formulario";
import ListaTareas from "./components/ListaTareas";

function App() {

  // useState para almacenar el array de tareas 📂 ├── src/app.jsx
  //📍snippet ⇒ React-estado-tareas
  const [tareas, setTareas] = useState([]);
  
  // useEffect con función de carga(arrowFunction)
  //📍snippet ⇒ React-useEffect-load
  useEffect(() => {
    // Función fetch para cargar tareas desde FastAPI
    // 📍snippet ⇒ React-fetch-loadTareas
      fetch("http://localhost:8000/tareas")
        .then((res) => res.json())
        .then((data) => setTareas(data));
  }, []);



// Pantalla genérica que muestra título, formulario y lista. 📂 ├── src/App.jsx
// 📍snippet ⇒ React-pantalla-principal-generica
return (
  <div className="p-8 max-w-xl mx-auto">
    <h1 className="text-2xl font-bold mb-4">📋 Lista Tareas</h1>
    <Formulario setTareas={setTareas} />
    <ListaTareas tareas={tareas} setTareas={setTareas} />
  </div>
);

}

 
export default App;