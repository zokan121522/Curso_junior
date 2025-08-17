export default function Card() {
  return (
    <div className="bg-white shadow-2xl rounded-2xl overflow-hidden max-w-sm transition hover:scale-105 hover:shadow-black/30 duration-300">
      <img
        src="https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?auto=format&fit=crop&w=800&q=80"
        alt="Imagen segura"
        className="w-full h-48 object-cover"
      />
      <div className="p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">Título de la tarjeta</h2>
        <p className="text-gray-600 mb-4">
          Esta es una descripción de ejemplo. Puedes personalizarla como quieras para destacar tu contenido.
        </p>
        <button className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white px-4 py-2 rounded-lg font-medium transition-all">
          Ver más
        </button>
      </div>
    </div>
  )
}
