// 🗂️ PASOS LÓGICOS RESUMIDOS:
// 1️⃣ Define función componente y expórtala.
// 2️⃣ Crea array de objetos con nombre y edad.
// 3️⃣ Devuelve un contenedor general.
// 4️⃣ Añade título descriptivo.
// 5️⃣ Recorre array con método de iteración.
// 6️⃣ Extrae propiedades de cada objeto.
// 7️⃣ Genera elemento repetido con clave única.
// 8️⃣ Muestra nombre y edad en frase.

export default function ListaObjetos(){
    const familia = [
            {nombre:"Ian", edad:13},
            {nombre:"Zoe", edad:10},
            {nombre:"Kai", edad:2}
    ];
    return(
        <div>
            <h3>Familia</h3>
            {familia.map((miembro)=>(
                <p key={miembro}>
                    {miembro.nombre} tiene {miembro.edad}
                </p>
            ))}
        </div>
    )
}