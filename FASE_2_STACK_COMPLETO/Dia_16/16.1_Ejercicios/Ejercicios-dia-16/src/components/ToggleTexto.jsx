import { useState } from "react";

export default function ToggleTexto(){
    const [visible,setVisible] = useState(true)
    return (
        <div>
            <button onClick={()=>setVisible(!visible)}>
                {visible? 'Ocultar': 'Mostrar'}
            </button>
            {visible && <p>Este es el texto visible</p>}
        </div>
    );
}