# 📚 DICCIONARIO EXTENDIDO DE JAVASCRIPT

Una tabla de consulta con **Nombre**, **Definición**, **Ejemplo** y **Analogía** para entender y recordar todos los conceptos clave de JavaScript.

---

| 🏷️ **Nombre** | 📖 **Definición** | 💻 **Ejemplo** | 🔍 **Analogía** |
|----------------|-------------------|----------------|-----------------|
| **Variable (let)** | Contenedor que guarda datos y puede cambiar. | `let edad = 25;` | 🗃️ Caja reutilizable. |
| **Constante (const)** | Valor fijo que no cambia. | `const PI = 3.1415;` | 🔒 Caja sellada. |
| **Var** | Variable con scope de función (obsoleta). | `var nombre = "Ana";` | 🕰️ Caja antigua con fugas. |
| **String** | Texto. | `"Hola mundo"` | 📝 Carta escrita. |
| **Number** | Número entero o decimal. | `42`, `3.14` | 🔢 Calculadora. |
| **Boolean** | Verdadero o falso. | `true`, `false` | 🔌 Interruptor ON/OFF. |
| **Array** | Lista ordenada de elementos. | `[1, 2, 3]` | 📚 Fila de casilleros. |
| **Objeto (Object)** | Datos clave-valor. | `{ nombre: "Ana" }` | 📇 Ficha de personaje. |
| **Null** | Valor vacío intencional. | `let coche = null;` | 🗑️ Caja vacía. |
| **Undefined** | Valor no asignado. | `let x;` | 📦 Caja olvidada. |
| **NaN** | Resultado no numérico. | `parseInt("Hola")` | ❌ Error de calculadora. |
| **Infinity** | Infinito matemático. | `1 / 0` | ♾️ Abismo sin fin. |
| **Operator** | Símbolo para operar. | `+`, `-` | 🛠️ Herramientas. |
| **Template Literal** | String con variables `${}`. | `` `Hola ${nombre}` `` | ✉️ Carta con huecos. |
| **Destructuring** | Extraer valores. | `const { nombre } = persona;` | 🎒 Vaciar mochila. |
| **Spread Operator** | Expande arrays/objetos. | `[...arr1, ...arr2]` | 📦 Mezclar cajas. |
| **Rest Operator** | Agrupa restos en array. | `function sum(...nums)` | 🎒 Bolsa con restos. |
| **Function** | Bloque reutilizable. | `function saludar() {}` | ☕ Cafetera. |
| **Arrow Function** | Sintaxis corta. | `const suma = (a,b) => a+b;` | 🏃 Versión express. |
| **Callback** | Función que se pasa. | `setTimeout(()=>{},1000)` | 🔔 Campana que suena. |
| **Promise** | Resultado asíncrono. | `fetch(url).then()` | 📦 Paquete en camino. |
| **Async/Await** | Espera Promises. | `await fetch(url)` | ⏸️ Pausa controlada. |
| **Try/Catch** | Maneja errores. | `try {} catch {}` | 🛟 Colchón seguridad. |
| **Throw** | Lanza error manual. | `throw new Error()` | 🚨 Alarma. |
| **JSON** | Formato de datos. | `JSON.stringify(obj)` | 🎒 Maleta ordenada. |
| **Parse/Stringify** | Objeto <-> JSON. | `JSON.parse()` | 🗣️ Traductor. |
| **Event Listener** | Detecta eventos. | `btn.addEventListener()` | 👂 Sensor. |
| **DOM** | Árbol de HTML. | `document.getElementById()` | 🌳 Árbol genealógico. |
| **Query Selector** | Busca en DOM. | `.querySelector(".clase")` | 🔎 Búsqueda rápida. |
| **Hoisting** | JS mueve declaraciones arriba. | `console.log(a); var a = 2;` | 🧹 Levantar alfombra. |
| **Scope** | Ámbito variable. | `{ let x = 2; }` | 🫧 Burbuja local. |
| **Closure** | Función que recuerda contexto. | `function padre() { let x=1; return function() { console.log(x); }}` | 🔐 Caja fuerte. |
| **This** | Contexto actual. | `this.nombre` | 👤 “Yo mismo”. |
| **Prototype** | Herencia objetos. | `Array.prototype` | 🧬 Molde genético. |
| **Class** | Plano de objeto. | `class Persona {}` | 🏠 Plano de casa. |
| **Instance** | Objeto real de clase. | `new Persona()` | 🏡 Casa construida. |
| **Constructor** | Inicializa instancia. | `constructor(nombre) {}` | 🚪 Puerta de entrada. |
| **Static Method** | Método solo de clase. | `static info() {}` | 🏭 Timbre de fábrica. |
| **Import/Export** | Compartir entre archivos. | `import x from './'` | 🚪 Puerta modular. |
| **Module** | Archivo reutilizable. | `import suma` | 🧩 Pieza LEGO. |
| **Map** | Clave-valor flexible. | `new Map()` | 📞 Lista contactos. |
| **Set** | Valores únicos. | `new Set([1,2])` | 🎟️ Lista VIP. |
| **Symbol** | Valor único. | `Symbol()` | 🆔 Huella digital. |
| **WeakMap/WeakSet** | Referencias débiles. | `new WeakMap()` | 🗑️ Caja autodestructible. |
| **Fetch** | Petición HTTP. | `fetch('url')` | 📬 Mensajero. |
| **CORS** | Restricción de orígenes. | `fetch()` con error. | 🔐 Puerta cerrada. |
| **Event Bubbling** | Evento sube DOM. | Click en botón. | 🍂 Hoja que cae de rama en rama. |
| **Event Capturing** | Captura de arriba a abajo. | `addEventListener('click', fn, true)` | 🔭 Lupa inversa. |
| **Debounce** | Retrasa ejecución. | Input search. | ⏳ Esperar silencio. |
| **Throttle** | Limita ejecución. | Scroll handler. | 🚦 Válvula reguladora. |
| **Regex** | Patrón texto. | `/\d+/` | 🕵️ Detector huellas. |
| **IIFE** | Función autoejecutable. | `(function(){})();` | 🚀 Lanzamiento inmediato. |
| **Promise.all** | Varias Promises a la vez. | `Promise.all([p1,p2])` | 👫 Todo el equipo llega. |
| **Promise.race** | Gana primera Promise. | `Promise.race([p1,p2])` | 🏁 Carrera de coches. |
| **Optional Chaining** | Acceso seguro. | `obj?.prop` | 🧐 Lupa cuidadosa. |
| **Nullish Coalescing** | Valor si null/undefined. | `x ?? 'default'` | 📌 Plan B. |
| **BigInt** | Números enormes. | `1234567890n` | 🗄️ Caja gigante. |
| **Strict Mode** | Modo estricto. | `'use strict';` | 📏 Reglas estrictas. |
| **Eval()** | Ejecuta string como código. | `eval("2+2")` | 🔓 Caja sin cerradura. |
| **Debugger** | Pausa código. | `debugger;` | ⏸️ Botón pausa tiempo. |
| **Data Attributes** | Atributos `data-` HTML. | `<div data-id="1">` | 🏷️ Post-it extra. |

---

## ✅ Tips

- 📌 **Guarda este .md en Notion/Obsidian.**
- 🧩 Úsalo como tarjetas Anki para repasar.
- 🔗 Añade ejemplos tuyos reales para cada concepto.

---

**🚀 Si quieres, puedo hacerte la versión `.csv` o transformarlo en tarjetas interactivas. Solo dilo.**