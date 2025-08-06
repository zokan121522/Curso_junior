// src/components/Card.jsx
export default function Card ({title,desc,image}){

  return(

    <div className="bg-green-600, rounded-lg, shadow-md, max-w-sm, p-6 border border-yellow-500 rounded-xl ">
      <img 
        src={image} className="w-full h-48 object-cover py-6 px-3"/>

      <h2 className="text-3xl font-bold text-red-600 mt-4  text-center">{title}</h2>

      <p className="text-gray-600 mt-2"> {desc} </p>

      <button className="bg-blue-600 text-white px-4 py-1 rounded-xl hover:bg-blue-300 transition mt-10">
        Boton
      </button>



    </div>

  )
  
  

}