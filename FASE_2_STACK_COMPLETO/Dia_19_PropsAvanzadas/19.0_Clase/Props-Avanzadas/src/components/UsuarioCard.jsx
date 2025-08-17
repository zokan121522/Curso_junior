import InfoExtra from "./InfoExtra";

export default function UsuarioCard ({nombre,edad,ciudad,hobby}) {
    return(
        <div className="bg-white shadow p-4 rounded">
            <h2 className="text-xl font-bold">{nombre}</h2>
            <p className="text-gray-700">Edad: {edad}</p>
            <InfoExtra ciudad={ciudad} hobby={hobby}/>
        </div>
    )
}