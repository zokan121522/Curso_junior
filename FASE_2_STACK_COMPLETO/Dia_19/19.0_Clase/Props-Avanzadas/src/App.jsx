import { usuarios } from "./data/usuarios";
import UsuarioCard from "./components/UsuarioCard";

export default function App (){

  return(
    <div className="p-6 grid sm:grid-cols-2 gap-6">
      {usuarios.map(usuario =>(
        <UsuarioCard
        key={usuario.id}
        {...usuario}
      />
      ))}
    </div>
  )

}

