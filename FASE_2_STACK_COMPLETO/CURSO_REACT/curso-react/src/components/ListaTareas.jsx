// 🗂️ PASOS LÓGICOS COMPLETOS:
// 1️⃣ Crea la función componente y expórtala con export default.
// 2️⃣ Define array de tareas dentro de la función.
// 3️⃣ Devuelve return con <div> contenedor.
// 4️⃣ Añade un <h2> como título.
// 5️⃣ Usa <ul> para lista.
// 6️⃣ Dentro del <ul>, usa .map() para recorrer tareas.
// 7️⃣ Devuelve un <li> por tarea con key única.

export default function ListaTareas(){
    const Lista = ["comprar","comer","dormir"]
    return (
        <div>
            <h3>Lista de tareas</h3>
            <ul>
                {Lista.map((tarea)=>(
                    <li key={tarea}>{tarea}</li>
                ))}
            </ul>
        </div>
    )
}