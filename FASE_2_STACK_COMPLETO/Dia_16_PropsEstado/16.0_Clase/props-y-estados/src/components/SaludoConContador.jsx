// src/components/SaludoConContador.jsx
import { useState } from "react";
export default function SaludoConContador({nombre}){
    const[contador,setContador] = useState(0);
    return(
        <div>
            {/* 2) Mostrar saludo con prop */}
            <h2>Hola, {nombre}</h2>
            
            {/* 3) Mostrar cuántos clicks */}
            <p> Has hecho click {contador} veces.</p>

            {/* 4) Botón para aumentar */}
            <button onClick={()=> setContador(contador +1)}>
                Click aquí!
            </button>
        </div>
    );
}
