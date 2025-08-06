



export default function TarjetaProducto({ titulo, descripcion, precio, imagen, destacado }) {
    const bordeClase = destacado ? 'border-yellow-500' : 'border-gray-200';

    return(
            <div className={`bg-white rounded-xl overflow-hidden max-w-sm border-2 ${bordeClase} shadow-md`}>

        <img
                src={imagen}
                alt={titulo}
                className="w-full h-48 object-cover"
            />
        
            <div className="p-6">
                <h2 className="text-xl font-bold text-gray-800">{titulo}</h2>
                <p className="text-gray-600 mt-2">{descripcion}</p>
                <p className="text-green-600 font-semibold mt-2">{precio.toFixed(2)}</p>
                <button className="w-full bg-blue-500 text-white py-2 px-4 rounded mt-4 hover:bg-blue-800 transition">
                    Comprar
                </button>
            </div>

        </div>
        
    )
}   