import { useState } from 'react'
import FormularioPerfil from './components/FormularioPerfil'



function App() {
  const [count, setCount] = useState(0)

  return (
    <h1>
      Formulario
      <FormularioPerfil/>
        
    </h1>


)
}

export default App
