import { useState } from "react";
export default function Checkbox (){

    const [aceptado,setAceptado] = useState(false);
    
    return(
        <div>
            <h3>Checkbox</h3>
            <label>
                <input
                    type="checkbox"
                    checked={aceptado}
                    onChange={(e)=> setAceptado(e.target.checked)}
                />
                Acepto los terminos
            </label>
            <br />
            <button disabled={!aceptado}>Enviar</button>
        </div>
    )


}