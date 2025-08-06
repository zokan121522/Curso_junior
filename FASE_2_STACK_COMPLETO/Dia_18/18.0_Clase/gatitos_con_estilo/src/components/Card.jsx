// src/components/Cards.jsx

export default function Card({ title, desc, image }) {
  return (
    <div className="bg-white shadow-2xl rounded-2xl overflow-hidden max-w-sm transition hover:scale-105 hover:shadow-black/30 duration-300">
      <img src={image} alt={title} className="w-full h-48 object-cover" />
      <div className="p-6">
        <h2 className="text-2xl font-bold text-red-800 mb-2">{title}</h2>
        <p className="text-yellow-600 mb-4">{desc}</p>
        <button className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white px-4 py-2 rounded-lg font-medium transition-all">
          Ver más
        </button>
      </div>
    </div>
  )
}