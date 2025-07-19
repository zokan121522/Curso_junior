// 🗂️ PASOS LÓGICOS RESUMIDOS:
// 1️⃣ Define la función componente y expórtala.
// 2️⃣ Dentro, crea un array de objetos con id, name y url de imagen.
// 3️⃣ Devuelve un contenedor general <div>.
// 4️⃣ Añade un título descriptivo <h3>.
// 5️⃣ Recorre el array con método de iteración.
// 6️⃣ Por cada objeto, genera un elemento repetido con key única.
// 7️⃣ Muestra imagen usando la url del objeto.
// 📸 URLs usadas:
// 🐶 Dog: https://cdn.outsideonline.com/wp-content/uploads/2023/03/Funny_Dog_H.jpg?crop=16:9&width=960&enable=upscale&quality=100
// 🐱 Cat: https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR1C0XX0G2NSOp5mmXPK6gwcRaZdCdmm3AQopYkwtzWCqfsv_VN06S8YeJZKyT7CnEmqo286gVeCHSUI2T3h7Z3zA
// 🐦 Bird: https://naturealberta.ca/wp-content/uploads/2025/04/6.-Tree-Swallow-NICK-CARTER-768x670.jpg


export default function ListaAnimals() {
  const animals = [
    {
      id: 1,
      name: "dog",
      img: "https://cdn.outsideonline.com/wp-content/uploads/2023/03/Funny_Dog_H.jpg?crop=16:9&width=960&enable=upscale&quality=100"
    },
    {
      id: 2,
      name: "cat",
      img: "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR1C0XX0G2NSOp5mmXPK6gwcRaZdCdmm3AQopYkwtzWCqfsv_VN06S8YeJZKyT7CnEmqo286gVeCHSUI2T3h7Z3zA"
    },
    {
      id: 3,
      name: "bird",
      img: "https://naturealberta.ca/wp-content/uploads/2025/04/6.-Tree-Swallow-NICK-CARTER-768x670.jpg"
    }
  ]

  return(
    <div>
        <h3>Animales:</h3>
        {animals.map(animal => (
            <div key={animal.name}>
                <img src={animal.img} width={200}/>
            </div>

        ))};

    </div>
  )
}