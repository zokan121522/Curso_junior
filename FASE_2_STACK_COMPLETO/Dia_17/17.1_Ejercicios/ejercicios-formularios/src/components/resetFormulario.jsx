



// 🧠 PASOS LÓGICOS DEL FORMULARIO CON RESET:
// 1. Importar useState desde React.
// 2. Definir tres estados: nombre, email y checkbox.
// 3. Crear función resetear que limpia todos los estados.
// 4. Devolver el formulario:
//    - Input controlado para nombre.
//    - Input controlado para email.
//    - Checkbox que actualiza estado aceptado.
//    - Botón que ejecuta la función reset cuando se hace click.



import { useState } from "react";
export default function ResetFormulario(){

    const [nombre,setNombre] = useState ("");
    const [email,setEmail] = useState ("");
    const [aceptado,setAceptado] = useState (false)

    const resetear = () => {
        setNombre("");
        setEmail("");
        setAceptado(false);
    };

    return (

        <div>
            <h3>Formulario con Reset</h3>

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
                onChange={(e)=> setEmail(e.target.value)}    
            />

            <label>
                <input 
                    type="checkbox"
                    checked= {aceptado}
                    onChange={(e)=> setAceptado(e.target.checked)}    
                />
            Aceptado
            </label>

            <button onClick={resetear}>Resetear</button>


        </div>



    );
    
}