import Checkbox from "./components/checkbox";
import FormularioEmail from "./components/formularioEmail";
import FormularioValidado from "./components/formularioValidado";
import ResetFormulario from "./components/resetFormulario";


export default function App() {
  return (
    <div>
      <h1>Mi App React Limpia 🚀</h1>
      {/* Aquí irán tus componentes */}
      <FormularioEmail/>
      <Checkbox/>
      <FormularioValidado/>
      <ResetFormulario/>
    </div>
  )
}
