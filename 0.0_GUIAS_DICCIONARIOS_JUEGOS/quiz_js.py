# quiz_js.py
# 🧠 QUIZ INTERACTIVO – DICCIONARIO JAVASCRIPT COMPLETO
# Con pista (analogía) antes de la definición
# Autor: Zokan & ChatGPT

import random

# -----------------------------------------------
# 📚 Diccionario completo
# -----------------------------------------------

diccionario = [
    {"nombre": "Variable (let)", "definicion": "Contenedor que guarda datos y puede cambiar.", "ejemplo": "let edad = 25;", "analogia": "🗃️ Caja reutilizable."},
    {"nombre": "Constante (const)", "definicion": "Valor fijo que no cambia.", "ejemplo": "const PI = 3.1415;", "analogia": "🔒 Caja sellada."},
    {"nombre": "Var", "definicion": "Variable con scope de función (obsoleta).", "ejemplo": "var nombre = \"Ana\";", "analogia": "🕰️ Caja antigua con fugas."},
    {"nombre": "String", "definicion": "Texto.", "ejemplo": "\"Hola mundo\"", "analogia": "📝 Carta escrita."},
    {"nombre": "Number", "definicion": "Número entero o decimal.", "ejemplo": "42, 3.14", "analogia": "🔢 Calculadora."},
    {"nombre": "Boolean", "definicion": "Verdadero o falso.", "ejemplo": "true, false", "analogia": "🔌 Interruptor ON/OFF."},
    {"nombre": "Array", "definicion": "Lista ordenada de elementos.", "ejemplo": "[1, 2, 3]", "analogia": "📚 Fila de casilleros."},
    {"nombre": "Objeto (Object)", "definicion": "Datos clave-valor.", "ejemplo": "{ nombre: \"Ana\" }", "analogia": "📇 Ficha de personaje."},
    {"nombre": "Null", "definicion": "Valor vacío intencional.", "ejemplo": "let coche = null;", "analogia": "🗑️ Caja vacía."},
    {"nombre": "Undefined", "definicion": "Valor no asignado.", "ejemplo": "let x;", "analogia": "📦 Caja olvidada."},
    {"nombre": "NaN", "definicion": "Resultado no numérico.", "ejemplo": "parseInt(\"Hola\")", "analogia": "❌ Error de calculadora."},
    {"nombre": "Infinity", "definicion": "Infinito matemático.", "ejemplo": "1 / 0", "analogia": "♾️ Abismo sin fin."},
    {"nombre": "Operator", "definicion": "Símbolo para operar.", "ejemplo": "+, -", "analogia": "🛠️ Herramientas."},
    {"nombre": "Template Literal", "definicion": "String con variables `${}`.", "ejemplo": "`Hola ${nombre}`", "analogia": "✉️ Carta con huecos."},
    {"nombre": "Destructuring", "definicion": "Extraer valores.", "ejemplo": "const { nombre } = persona;", "analogia": "🎒 Vaciar mochila."},
    {"nombre": "Spread Operator", "definicion": "Expande arrays/objetos.", "ejemplo": "[...arr1, ...arr2]", "analogia": "📦 Mezclar cajas."},
    {"nombre": "Rest Operator", "definicion": "Agrupa restos en array.", "ejemplo": "function sum(...nums)", "analogia": "🎒 Bolsa con restos."},
    {"nombre": "Function", "definicion": "Bloque reutilizable.", "ejemplo": "function saludar() {}", "analogia": "☕ Cafetera."},
    {"nombre": "Arrow Function", "definicion": "Sintaxis corta.", "ejemplo": "const suma = (a,b) => a+b;", "analogia": "🏃 Versión express."},
    {"nombre": "Callback", "definicion": "Función que se pasa.", "ejemplo": "setTimeout(()=>{},1000)", "analogia": "🔔 Campana que suena."},
    {"nombre": "Promise", "definicion": "Resultado asíncrono.", "ejemplo": "fetch(url).then()", "analogia": "📦 Paquete en camino."},
    {"nombre": "Async/Await", "definicion": "Espera Promises.", "ejemplo": "await fetch(url)", "analogia": "⏸️ Pausa controlada."},
    {"nombre": "Try/Catch", "definicion": "Maneja errores.", "ejemplo": "try {} catch {}", "analogia": "🛟 Colchón seguridad."},
    {"nombre": "Throw", "definicion": "Lanza error manual.", "ejemplo": "throw new Error()", "analogia": "🚨 Alarma."},
    {"nombre": "JSON", "definicion": "Formato de datos.", "ejemplo": "JSON.stringify(obj)", "analogia": "🎒 Maleta ordenada."},
    {"nombre": "Parse/Stringify", "definicion": "Objeto <-> JSON.", "ejemplo": "JSON.parse()", "analogia": "🗣️ Traductor."},
    {"nombre": "Event Listener", "definicion": "Detecta eventos.", "ejemplo": "btn.addEventListener()", "analogia": "👂 Sensor."},
    {"nombre": "DOM", "definicion": "Árbol de HTML.", "ejemplo": "document.getElementById()", "analogia": "🌳 Árbol genealógico."},
    {"nombre": "Query Selector", "definicion": "Busca en DOM.", "ejemplo": ".querySelector(\".clase\")", "analogia": "🔎 Búsqueda rápida."},
    {"nombre": "Hoisting", "definicion": "JS mueve declaraciones arriba.", "ejemplo": "console.log(a); var a = 2;", "analogia": "🧹 Levantar alfombra."},
    {"nombre": "Scope", "definicion": "Ámbito variable.", "ejemplo": "{ let x = 2; }", "analogia": "🫧 Burbuja local."},
    {"nombre": "Closure", "definicion": "Función que recuerda contexto.", "ejemplo": "function padre() { let x=1; return function() { console.log(x); } }", "analogia": "🔐 Caja fuerte."},
    {"nombre": "This", "definicion": "Contexto actual.", "ejemplo": "this.nombre", "analogia": "👤 “Yo mismo”."},
    {"nombre": "Prototype", "definicion": "Herencia objetos.", "ejemplo": "Array.prototype", "analogia": "🧬 Molde genético."},
    {"nombre": "Class", "definicion": "Plano de objeto.", "ejemplo": "class Persona {}", "analogia": "🏠 Plano de casa."},
    {"nombre": "Instance", "definicion": "Objeto real de clase.", "ejemplo": "new Persona()", "analogia": "🏡 Casa construida."},
    {"nombre": "Constructor", "definicion": "Inicializa instancia.", "ejemplo": "constructor(nombre) {}", "analogia": "🚪 Puerta de entrada."},
    {"nombre": "Static Method", "definicion": "Método solo de clase.", "ejemplo": "static info() {}", "analogia": "🏭 Timbre de fábrica."},
    {"nombre": "Import/Export", "definicion": "Compartir entre archivos.", "ejemplo": "import x from './'", "analogia": "🚪 Puerta modular."},
    {"nombre": "Module", "definicion": "Archivo reutilizable.", "ejemplo": "import suma", "analogia": "🧩 Pieza LEGO."},
    {"nombre": "Map", "definicion": "Clave-valor flexible.", "ejemplo": "new Map()", "analogia": "📞 Lista contactos."},
    {"nombre": "Set", "definicion": "Valores únicos.", "ejemplo": "new Set([1,2])", "analogia": "🎟️ Lista VIP."},
    {"nombre": "Symbol", "definicion": "Valor único.", "ejemplo": "Symbol()", "analogia": "🆔 Huella digital."},
    {"nombre": "WeakMap/WeakSet", "definicion": "Referencias débiles.", "ejemplo": "new WeakMap()", "analogia": "🗑️ Caja autodestructible."},
    {"nombre": "Fetch", "definicion": "Petición HTTP.", "ejemplo": "fetch('url')", "analogia": "📬 Mensajero."},
    {"nombre": "CORS", "definicion": "Restricción de orígenes.", "ejemplo": "fetch() con error.", "analogia": "🔐 Puerta cerrada."},
    {"nombre": "Event Bubbling", "definicion": "Evento sube DOM.", "ejemplo": "Click en botón.", "analogia": "🍂 Hoja que cae de rama en rama."},
    {"nombre": "Event Capturing", "definicion": "Captura de arriba a abajo.", "ejemplo": "addEventListener('click', fn, true)", "analogia": "🔭 Lupa inversa."},
    {"nombre": "Debounce", "definicion": "Retrasa ejecución.", "ejemplo": "Input search.", "analogia": "⏳ Esperar silencio."},
    {"nombre": "Throttle", "definicion": "Limita ejecución.", "ejemplo": "Scroll handler.", "analogia": "🚦 Válvula reguladora."},
    {"nombre": "Regex", "definicion": "Patrón texto.", "ejemplo": "/\\d+/", "analogia": "🕵️ Detector huellas."},
    {"nombre": "IIFE", "definicion": "Función autoejecutable.", "ejemplo": "(function(){})();", "analogia": "🚀 Lanzamiento inmediato."},
    {"nombre": "Promise.all", "definicion": "Varias Promises a la vez.", "ejemplo": "Promise.all([p1,p2])", "analogia": "👫 Todo el equipo llega."},
    {"nombre": "Promise.race", "definicion": "Gana primera Promise.", "ejemplo": "Promise.race([p1,p2])", "analogia": "🏁 Carrera de coches."},
    {"nombre": "Optional Chaining", "definicion": "Acceso seguro.", "ejemplo": "obj?.prop", "analogia": "🧐 Lupa cuidadosa."},
    {"nombre": "Nullish Coalescing", "definicion": "Valor si null/undefined.", "ejemplo": "x ?? 'default'", "analogia": "📌 Plan B."},
    {"nombre": "BigInt", "definicion": "Números enormes.", "ejemplo": "1234567890n", "analogia": "🗄️ Caja gigante."},
    {"nombre": "Strict Mode", "definicion": "Modo estricto.", "ejemplo": "'use strict';", "analogia": "📏 Reglas estrictas."},
    {"nombre": "Eval()", "definicion": "Ejecuta string como código.", "ejemplo": "eval(\"2+2\")", "analogia": "🔓 Caja sin cerradura."},
    {"nombre": "Debugger", "definicion": "Pausa código.", "ejemplo": "debugger;", "analogia": "⏸️ Botón pausa tiempo."},
    {"nombre": "Data Attributes", "definicion": "Atributos `data-` HTML.", "ejemplo": "<div data-id=\"1\">", "analogia": "🏷️ Post-it extra."},
]

# -----------------------------------------------
# 🔁 Lógica principal del quiz
# -----------------------------------------------

def ejecutar_quiz():
    print("\n🚀 Bienvenido al QUIZ de JavaScript 🔥\n")
    seguir = True

    while seguir:
        termino = random.choice(diccionario)
        print(f"📌 Concepto: {termino['nombre']}\n")
        input("✏️ ¿Qué significa? Pulsa Enter si necesitas una pista...\n")

        print(f"🧩 PISTA (Analogía): {termino['analogia']}\n")
        input("❓ Pulsa Enter para ver la definición completa...\n")

        print(f"✅ Definición:\n{termino['definicion']}\n")
        print(f"💻 Ejemplo:\n{termino['ejemplo']}\n")

        respuesta = input("👉 ¿Quieres otro término? (s/n): ").strip().lower()
        if respuesta != "s":
            seguir = False

    print("\n🏆 ¡Bien jugado! Sigue practicando.\n")

# -----------------------------------------------
# ▶️ Ejecutar
# -----------------------------------------------

if __name__ == "__main__":
    ejecutar_quiz()