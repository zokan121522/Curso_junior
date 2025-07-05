// src/App.jsx

import SaludoConContador from "./components/SaludoConContador";

function App(){
  return(
    <div>
      <h1>Mini-reto: Props + useState</h1>
      {/* Usar componente y pasar prop nombre */}
      <SaludoConContador nombre="Zokan"/>

    </div>
  );
}

export default App ;