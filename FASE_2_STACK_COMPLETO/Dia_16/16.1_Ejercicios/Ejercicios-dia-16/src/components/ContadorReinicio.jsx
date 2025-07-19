// src/components/ContadorReinicio.jsx

import { useState } from "react";

export default function ContadorReinicio(){
    const[contador,setContador] = useState(0);

    return(
        <div>
            <p>Contador: {contador}</p>
            <button onClick={()=> setContador(contador + 1)}>
                +1
            </button>

            <button onClick={()=> setContador(0)}>
                Reiniciar
            </button>
        </div>
    );
}