
// ✅ src/App.jsx

import SaludoCondicional from "./components/SaludoCondicional";
import ContadorPaso from "./components/ContadorPaso";
import ContadorReinicio from "./components/ContadorReinicio";
import ListaNombres from "./components/ListaNombres";
import ToggleTexto from "./components/ToggleTexto";

function App(){
  return (
    <div>
      <SaludoCondicional esAdmin={false} />
      <ContadorPaso paso={10} />
      <ContadorReinicio/>
      <ListaNombres nombres={["Jaime","Jesica"]}/>
      <ToggleTexto/>
    </div>
  );
}

export default App