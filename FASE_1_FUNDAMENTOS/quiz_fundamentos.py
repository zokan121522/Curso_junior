
# quiz_fundamentos.py
# 🧠 QUIZ INTERACTIVO – FASE 1 FUNDAMENTOS (~50 preguntas + slots)
# Formato: {"nombre": ..., "definicion": ..., "ejemplo": ..., "analogia": ...}

import random

diccionario = [
    # VARIABLES & TIPOS DE DATOS
    {"nombre": "¿Qué es una variable?", "definicion": "Contenedor que guarda datos para reutilizarlos.", "ejemplo": "nombre = 'Zokan'", "analogia": "🗃️ Caja etiquetada."},
    {"nombre": "¿Qué es un string?", "definicion": "Cadena de caracteres.", "ejemplo": "mensaje = 'Hola mundo'", "analogia": "✉️ Carta."},
    {"nombre": "¿Qué es un int?", "definicion": "Número entero.", "ejemplo": "edad = 25", "analogia": "🔢 Entero puro."},
    {"nombre": "¿Qué es un float?", "definicion": "Número decimal.", "ejemplo": "altura = 1.75", "analogia": "🌊 Número con olas decimales."},
    {"nombre": "¿Qué es un boolean?", "definicion": "Valor True o False.", "ejemplo": "is_active = True", "analogia": "🔌 Interruptor ON/OFF."},
    {"nombre": "¿Qué es None?", "definicion": "Valor nulo, ausencia de valor.", "ejemplo": "respuesta = None", "analogia": "🗑️ Caja vacía."},
    {"nombre": "¿Cómo declarar múltiples variables?", "definicion": "Asignación múltiple en una línea.", "ejemplo": "a, b, c = 1, 2, 3", "analogia": "📦 Varias cajas juntas."},

    # OPERADORES
    {"nombre": "¿Qué hace +?", "definicion": "Suma números o concatena strings.", "ejemplo": "2+3, 'Hola'+'Mundo'", "analogia": "➕ Piezas unidas."},
    {"nombre": "¿Qué hace -?", "definicion": "Resta valores numéricos.", "ejemplo": "5 - 2 = 3", "analogia": "➖ Quitar piezas."},
    {"nombre": "¿Qué hace *?", "definicion": "Multiplica valores.", "ejemplo": "3 * 4 = 12", "analogia": "✖️ Paquetes repetidos."},
    {"nombre": "¿Qué hace /?", "definicion": "Divide valores.", "ejemplo": "10 / 2 = 5.0", "analogia": "➗ Partir pastel."},
    {"nombre": "¿Qué hace //?", "definicion": "División entera (sin decimales).", "ejemplo": "7 // 2 = 3", "analogia": "📏 Cortar solo partes completas."},
    {"nombre": "¿Qué hace %?", "definicion": "Resto de división.", "ejemplo": "10 % 3 = 1", "analogia": "🍰 Trozo que sobra."},

    # I/O
    {"nombre": "¿Para qué sirve print()?", "definicion": "Muestra texto en consola.", "ejemplo": "print('Hola')", "analogia": "📢 Megáfono."},
    {"nombre": "¿Para qué sirve input()?", "definicion": "Recibe texto del usuario.", "ejemplo": "nombre = input()", "analogia": "🎙️ Micrófono."},
    {"nombre": "¿Qué hace \n?", "definicion": "Salto de línea.", "ejemplo": "print('Hola\nMundo')", "analogia": "↩️ Enter en texto."},

    # CONDICIONALES
    {"nombre": "¿Qué hace if?", "definicion": "Ejecuta código si condición es True.", "ejemplo": "if x > 0:", "analogia": "🚦 Semáforo verde."},
    {"nombre": "¿Qué hace elif?", "definicion": "Otra condición si if es False.", "ejemplo": "elif x == 0:", "analogia": "🔄 Alternativa."},
    {"nombre": "¿Qué hace else?", "definicion": "Caso por defecto.", "ejemplo": "else:", "analogia": "🗂️ Cajón 'otros'."},
    {"nombre": "¿Qué hace and?", "definicion": "Verifica que ambas sean True.", "ejemplo": "if a > 0 and b > 0:", "analogia": "🔗 Doble candado."},
    {"nombre": "¿Qué hace or?", "definicion": "True si una es True.", "ejemplo": "if a > 0 or b > 0:", "analogia": "🔀 Camino alternativo."},

    # BUCLES
    {"nombre": "¿Qué hace for?", "definicion": "Itera sobre secuencia.", "ejemplo": "for i in range(5):", "analogia": "🔁 Repetidor automático."},
    {"nombre": "¿Qué hace while?", "definicion": "Repite mientras condición True.", "ejemplo": "while x < 5:", "analogia": "♾️ Tornillo sin fin."},
    {"nombre": "¿Qué hace break?", "definicion": "Sale del bucle.", "ejemplo": "break", "analogia": "⛔ Freno de emergencia."},
    {"nombre": "¿Qué hace continue?", "definicion": "Salta a siguiente iteración.", "ejemplo": "continue", "analogia": "⏭️ Botón siguiente."},

    # LISTAS
    {"nombre": "¿Qué es una lista?", "definicion": "Colección ordenada.", "ejemplo": "frutas = ['manzana','pera']", "analogia": "📚 Fila de casilleros."},
    {"nombre": "¿Para qué sirve append()?", "definicion": "Añade elemento al final.", "ejemplo": "lista.append('nuevo')", "analogia": "📌 Pin extra."},
    {"nombre": "¿Qué hace len()?", "definicion": "Devuelve número de elementos.", "ejemplo": "len(lista)", "analogia": "📏 Regla para contar."},

    # FUNCIONES
    {"nombre": "¿Qué es una función?", "definicion": "Bloque reutilizable.", "ejemplo": "def saludar():", "analogia": "☕ Cafetera."},
    {"nombre": "¿Para qué sirve return?", "definicion": "Devuelve valor.", "ejemplo": "return x", "analogia": "🎫 Tique de salida."},
    {"nombre": "¿Qué es parámetro?", "definicion": "Variable dentro de función.", "ejemplo": "def suma(a,b):", "analogia": "🎯 Ranura para datos."},

    # ARCHIVOS
    {"nombre": "¿Cómo abrir archivo lectura?", "definicion": "Modo 'r'.", "ejemplo": "open('file.txt','r')", "analogia": "📖 Abrir libro."},
    {"nombre": "¿Cómo abrir archivo escritura?", "definicion": "Modo 'w'.", "ejemplo": "open('file.txt','w')", "analogia": "✍️ Página nueva."},

    # GIT
    {"nombre": "¿Qué hace git init?", "definicion": "Crea repo vacío.", "ejemplo": "git init", "analogia": "📦 Caja fuerte vacía."},
    {"nombre": "¿Qué hace git add?", "definicion": "Prepara archivos.", "ejemplo": "git add file.py", "analogia": "🛒 Meter al carrito."},
    {"nombre": "¿Qué hace git commit?", "definicion": "Guarda snapshot.", "ejemplo": "git commit -m 'mensaje'", "analogia": "📸 Foto para el álbum."},

        # ERRORES COMUNES
    {"nombre": "¿Qué es un TypeError al sumar string + int?",
     "definicion": "Error que ocurre cuando intentas operar tipos incompatibles, como string con número.",
     "ejemplo": "'Edad: ' + 5  # TypeError",
     "analogia": "🧩 Piezas que no encajan."},

    {"nombre": "¿Qué es un IndentationError?",
     "definicion": "Error por mala indentación del código, como no alinear bloques correctamente.",
     "ejemplo": "if True:\\n  print('Hola')  # correcto\\nprint('Hola')  # IndentationError",
     "analogia": "📏 Regla torcida: línea mal alineada."},

    # BUCLES ANIDADOS Y FLUJOS
    {"nombre": "¿Qué es un bucle for anidado?",
     "definicion": "Un bucle for dentro de otro for, útil para recorrer estructuras de datos en varias dimensiones.",
     "ejemplo": "for i in range(3):\\n  for j in range(2):\\n    print(i,j)",
     "analogia": "📚 Matrioshka: muñecas dentro de muñecas."},

    {"nombre": "¿Qué es un if dentro de while?",
     "definicion": "Estructura condicional dentro de un bucle que evalúa una condición repetidamente.",
     "ejemplo": "x = 0\\nwhile x < 5:\\n  if x == 3:\\n    break\\n  x += 1",
     "analogia": "🔄 Bucle con semáforo: rompe el ciclo cuando se cumple algo."},

    # DEBUG Y BUENAS PRÁCTICAS
    {"nombre": "¿Qué significa debuggear un script?",
     "definicion": "Proceso de revisar y corregir errores en el código paso a paso.",
     "ejemplo": "print(variable) para ver su valor en distintas partes.",
     "analogia": "🔍 Detective revisando pista por pista."},

    {"nombre": "¿Cuál es una buena práctica con comentarios?",
     "definicion": "Escribir comentarios claros y relevantes para explicar partes del código.",
     "ejemplo": "# Esto calcula el promedio de una lista",
     "analogia": "📝 Post-it que recuerda qué hace cada parte."},

    {"nombre": "¿Qué es un script multiusos?",
     "definicion": "Script genérico que puede resolver diferentes tareas mediante parámetros.",
     "ejemplo": "sumar.py que suma varios números según input",
     "analogia": "🛠️ Navaja suiza: sirve para varias cosas."},

    # GIT COMANDOS AVANZADOS
    {"nombre": "¿Qué hace git pull?",
     "definicion": "Actualiza tu repositorio local con cambios del remoto.",
     "ejemplo": "git pull origin main",
     "analogia": "🔄 Descargar las últimas versiones de la nube."},

    {"nombre": "¿Qué hace git push?",
     "definicion": "Envía tus cambios locales al repositorio remoto.",
     "ejemplo": "git push origin main",
     "analogia": "📤 Subir archivos a la nube."},

    {"nombre": "¿Qué es un archivo .gitignore?",
     "definicion": "Lista de archivos o carpetas que Git debe ignorar (no subir al repo).",
     "ejemplo": ".env\\n__pycache__/",
     "analogia": "🚫 Lista de cosas que no se guardan en la caja fuerte."},

        # CONTINUACIÓN PREGUNTAS 41–50

    # ERRORES COMUNES
    {"nombre": "¿Qué es un TypeError al sumar string + int?",
     "definicion": "Error que ocurre cuando intentas operar tipos incompatibles, como string con número.",
     "ejemplo": "'Edad: ' + 5  # TypeError",
     "analogia": "🧩 Piezas que no encajan."},

    {"nombre": "¿Qué es un IndentationError?",
     "definicion": "Error por mala indentación del código, como no alinear bloques correctamente.",
     "ejemplo": "if True:\\n  print('Hola')  # correcto\\nprint('Hola')  # IndentationError",
     "analogia": "📏 Regla torcida: línea mal alineada."},

    # BUCLES ANIDADOS Y FLUJOS
    {"nombre": "¿Qué es un bucle for anidado?",
     "definicion": "Un bucle for dentro de otro for, útil para recorrer estructuras de datos en varias dimensiones.",
     "ejemplo": "for i in range(3):\\n  for j in range(2):\\n    print(i,j)",
     "analogia": "📚 Matrioshka: muñecas dentro de muñecas."},

    {"nombre": "¿Qué es un if dentro de while?",
     "definicion": "Estructura condicional dentro de un bucle que evalúa una condición repetidamente.",
     "ejemplo": "x = 0\\nwhile x < 5:\\n  if x == 3:\\n    break\\n  x += 1",
     "analogia": "🔄 Bucle con semáforo: rompe el ciclo cuando se cumple algo."},

    # DEBUG Y BUENAS PRÁCTICAS
    {"nombre": "¿Qué significa debuggear un script?",
     "definicion": "Proceso de revisar y corregir errores en el código paso a paso.",
     "ejemplo": "print(variable) para ver su valor en distintas partes.",
     "analogia": "🔍 Detective revisando pista por pista."},

    {"nombre": "¿Cuál es una buena práctica con comentarios?",
     "definicion": "Escribir comentarios claros y relevantes para explicar partes del código.",
     "ejemplo": "# Esto calcula el promedio de una lista",
     "analogia": "📝 Post-it que recuerda qué hace cada parte."},

    {"nombre": "¿Qué es un script multiusos?",
     "definicion": "Script genérico que puede resolver diferentes tareas mediante parámetros.",
     "ejemplo": "sumar.py que suma varios números según input",
     "analogia": "🛠️ Navaja suiza: sirve para varias cosas."},

    # GIT COMANDOS AVANZADOS
    {"nombre": "¿Qué hace git pull?",
     "definicion": "Actualiza tu repositorio local con cambios del remoto.",
     "ejemplo": "git pull origin main",
     "analogia": "🔄 Descargar las últimas versiones de la nube."},

    {"nombre": "¿Qué hace git push?",
     "definicion": "Envía tus cambios locales al repositorio remoto.",
     "ejemplo": "git push origin main",
     "analogia": "📤 Subir archivos a la nube."},

    {"nombre": "¿Qué es un archivo .gitignore?",
     "definicion": "Lista de archivos o carpetas que Git debe ignorar (no subir al repo).",
     "ejemplo": ".env\\n__pycache__/",
     "analogia": "🚫 Lista de cosas que no se guardan en la caja fuerte."},
]

def ejecutar_quiz():
    print("\n🚀 Bienvenido al QUIZ FASE 1 FUNDAMENTOS (~50 preguntas) 🔥\n")
    seguir = True
    while seguir:
        termino = random.choice(diccionario)
        print(f"📌 Pregunta: {termino['nombre']}\n")
        input("✏️ ¿Sabes la respuesta? Pulsa Enter para pista...\n")
        print(f"🧩 PISTA (Analogía): {termino['analogia']}\n")
        input("❓ Pulsa Enter para ver la definición completa...\n")
        print(f"✅ Definición:\n{termino['definicion']}\n")
        print(f"💻 Ejemplo:\n{termino['ejemplo']}\n")
        respuesta = input("👉 ¿Otra pregunta? (s/n): ").strip().lower()
        if respuesta != "s":
            seguir = False
    print("\n🏆 ¡Bien jugado!\n")

if __name__ == "__main__":
    ejecutar_quiz()
