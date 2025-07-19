// 🗂️ PASOS LÓGICOS RESUMIDOS:
// 1️⃣ Define función componente y expórtala.
// 2️⃣ Crea array de categorías con sub-items.
// 3️⃣ Devuelve contenedor general.
// 4️⃣ Añade título descriptivo.
// 5️⃣ Recorre categorías con método de iteración.
// 6️⃣ Dentro, muestra nombre de categoría.
// 7️⃣ Recorre sub-items con método de iteración anidado.
// 8️⃣ Genera elementos con claves únicas y muestra cada item.


// 🗂️ PASOS LÓGICOS RESUMIDOS:
// 1️⃣ Define función componente y expórtala.
export default function ListaAnidada (){
// 2️⃣ Crea array de categorías con sub-items.
    const categorias =[
        {categoria: "fruta",items:["manzana","pera","sandia"]},
        {categoria: "animales",items:["perro","gato","tortuga"]}
    ]
// 3️⃣ Devuelve contenedor general.
    return (
        <div>
{/* 4️⃣ Añade título descriptivo.*/}
            <h3>Lista Anidada</h3>
{/* 5️⃣ Recorre categorías con método de iteración.*/}
            {categorias.map((nombre,index)=>(
 // 6️⃣ Dentro, muestra nombre de categoría.
                <div key={index}>
                    <h4>{nombre.categoria}</h4>
{/* 7️⃣ Recorre sub-items con método de iteración anidado.*/}
                    <ul>
                        {nombre.items.map((item,idx)=>(
// 8️⃣ Genera elementos con claves únicas y muestra cada item.
                            <li key={idx}>{item}</li>
                        ))}
                    </ul>
                </div>
               
            ))}
        </div>
    )
}