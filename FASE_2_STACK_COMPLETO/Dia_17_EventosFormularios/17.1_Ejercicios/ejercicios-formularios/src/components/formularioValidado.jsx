

// 1. Importamos useState
// 2. Definimos estados para nombre, email y checkbox
// 3. Creamos la lógica para validar campos
// 4. Devolvemos el formulario con inputs controlados y mensaje condicional

import { useState } from "react";

export default function FormularioValidado (){

    const [nombre,setNombre] = useState ("");
    const [email,setEmali] = useState ("");
    const [aceptado,setAceptado]= useState (false);

    const camposCompletos = nombre !==("") && email.includes("@") && aceptado;

    return (
        <div>
            <h3>Formulario con validación</h3>
            <input
             type="text"
             placeholder="Nombre"
             value={nombre}
             onChange={(e)=> setNombre(e.target.value)}
            />

            <input
             type="text" 
             placeholder="Email"
             value={email}
             onChange={(e)=> setEmali(e.target.value)} 
            />
            <label>
                <input
                 type="checkbox"
                 value={aceptado}
                 onChange={(e)=> setAceptado(e.target.checked)}   
                /> Aceptado
            </label>
            {camposCompletos && <p>Formulario completado correctamente</p>}

        </div>
    )

}