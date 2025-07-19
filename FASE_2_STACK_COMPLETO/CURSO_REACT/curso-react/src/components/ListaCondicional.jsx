//🗂️ PASOS LÓGICOS COMPLETOS (SIN CÓDIGO)
// 1️⃣ Crea una función que será tu componente y asegúrate de exportarla para poder usarla.
// 2️⃣ Dentro de esa función, define una lista que contenga valores booleanos (verdadero o falso).
// 3️⃣ Devuelve una estructura general que contenga un contenedor principal.
// 4️⃣ Dentro de ese contenedor, pon un título que describa lo que se va a mostrar.
// 5️⃣ Recorre la lista de valores uno a uno y obtén cada elemento junto con su posición.
// 6️⃣ Para cada elemento de la lista, crea un bloque visual individual identificado de forma única.
// 7️⃣ Dentro de cada bloque, evalúa la condición booleana.
// 8️⃣ Según si la condición es verdadera o falsa, muestra un mensaje diferente (por ejemplo: correcto o incorrecto) usando una comprobación condicional.

export default function ListaCondicional (){
    const lista = [false]

    return(
        <div>
            <h3>Lista condicional</h3>
            {lista.map((condicion,index) => (
                <p key={index}>
                    {condicion ? "verdadero" :"falso"}
                </p>
            ))}
        </div>
    );

}