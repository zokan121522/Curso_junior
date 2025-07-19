import {useState} from 'react';

export default function FormularioPerfil(){
    const [nombre,setNombre] = useState("");
    const [email,setEmail] = useState ("");
    const [aceptado,setAceptado] = useState(false);
    const [mensaje,setMesage] = useState("")


const manejarEnvio = (e) => {
    e.preventDefault();
    if (nombre === "" || !email.includes("@") || !aceptado){
        setMesage ("Completa todos los campos correctamente");
    }else{
            setMesage("Formulario enviado con exito");
        }
    };

const manejarReset = () => {
    setNombre("");
    setEmail("");
    setAceptado(false);
    setMesage("");
};

return (
    <form onSubmit= {manejarEnvio}>
        <h2> Formulario Perfil</h2>
        <input 
            type='text'
            placeholder='Tu nombre'
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
        />

        <input 
        type="email"
        placeholder='Tu mail'
        value={email}
        onChange={(e)=> setEmail(e.target.value)} 
        />

        <div>
            <input 
            type="checkbox" 
            checked={aceptado}
            onChange={(e)=> setAceptado(e.target.checked)}
            />
            <label>Acepto Términos</label>
        </div>

        <button type='submit' disabled={!aceptado}>
            Enviar
        </button>

        <button type='button' onClick={manejarReset}>
            Limpiar
        </button>

        {mensaje && <p>{mensaje}</p>}

    </form>
);

}
