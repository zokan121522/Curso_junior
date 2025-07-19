// 🗂️ PASOS LÓGICOS COMPLETOS:
// 1️⃣ Define la función componente y expórtala con export default.
// 2️⃣ Dentro, crea array nombres con varios valores.
// 3️⃣ Devuelve return con <div> contenedor general.
// 4️⃣ Añade <h2> como título descriptivo.
// 5️⃣ Usa <ul> para lista desordenada.
// 6️⃣ Dentro de <ul>, usa .map() con (nombre, index).
// 7️⃣ Devuelve <li> por nombre con key={index}.
// 8️⃣ Muestra índice + 1 y el nombre dentro del <li>.

export default function ListaConIndices() {
    const nombre =["Jaime","Jesica","Zokan"];
    return (
        <div>
            <h3>Lista con Condiciones</h3>
            <ul>
                {nombre.map((nombre,index) => (
                    <li key={index}> {index + 1}. {nombre} </li>
                ))}
            </ul>
        </div>
    );
    
}