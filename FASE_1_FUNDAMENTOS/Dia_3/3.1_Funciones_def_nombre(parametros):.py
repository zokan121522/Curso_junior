# 3.1_Funciones_def_nombre(parametros):.py

"""
def nombre(parametros):
    cuerpo_funcion
    return algo

def hacerTostada(pan):
    print(f"Tostando el pan:  {pan}")
    return f"{pan} tostado"
"""

"""
def saluda():
    print("Hola,¿como estas?")
saluda()
"""
# > Hola,¿como estas?

"""
def saludar(nombre):
    print(f"Hola, como estas {nombre}?")

saludar("jaime")
"""
# > Hola, como estas jaime?

"""
def despedirse(nombre):
    print(f"Hasta luego {nombre}")
despedirse("Jaime")
"""
# > Hasta luego Jaime

"""
def sumar(a,b):
    return a + b

resultado = sumar(5,3)
print("Resultado", resultado)
"""
# > Resultado 8

"""
def decir_hola():
    return "hola"

mensaje = decir_hola()
print(mensaje)
"""
# > hola

# 🧠 Analogía 2: Máquina expendedora
"""
dinero = float(input("Introduce el dinero.."))
def vending(cantidad):
    if cantidad >= 1.5:
        print("Toma la bebida")
    else:
        print("Dinero insuficiente")
print(vending(dinero))
"""


# 🧪 Ejercicio guiado paso a paso

# 1️⃣ Función que salude
"""
nombre = input("Como te llamas?")
def saludar(nombre):
    print(f"Hola, {nombre}")
saludar(nombre)
"""

# 2️⃣ Función que calcule área de triángulo
"""
base = float(input("Base = "))
altura = float(input("Altura = "))

def area (base,altura):
    return base * altura / 2

resultado = area (base,altura)
print(f"El area de la base {base} por altura {altura} es de {resultado}")
"""
# 📥 INPUT
# Base = 10
# Altura = 5
# 🛠️ FUNCIÓN
# Calcula: 10 * 5 / 2 = 25.0
# 📦 OUTPUT GUARDADO
# resultado = 25.0
# 📣 IMPRIME
"El área de la base 10.0 por altura 5.0 es de 25.0"


# 3️⃣ Ejercicio 3 – Clasificador de Edad 🧒👩‍🦱🧓
"""
Enunciado:
Crea una función llamada clasificar_edad que reciba un número entero (edad) y devuelva una cadena según estos rangos:
	•	Menor de 13 años → "Niño"
	•	Entre 13 y 17 años → "Adolescente"
	•	18 o más → "Adulto"

Después, pide al usuario su edad por consola, llama a la función y muestra el resultado con un mensaje como:

Tienes 15 años → Adolescente
💡 Usa return en la función, y print() fuera.
"""


"""
def clasificar_edad(edad):
    if edad < 13 :
        return "niño"
    elif edad < 17 :
        return "adolescente"
    else:
        return "adulto"

años = int(input("Cuantos años tienes..."))
clasificacion = clasificar_edad(años)

print (f"Tienes {años} años eres un {clasificacion} ")
"""

# 📥 INPUT  
# Usuario escribe: `15`
# 🛠️ FUNCIÓN  
# Se ejecuta:  
# python clasificar_edad(15)
# Proceso interno:
# 15 < 13 → ❌  
# 15 < 17 → ✅  
# → devuelve: "adolescente"
# 📦 OUTPUT GUARDADO
# clasificacion = "adolescente"
# 📣 IMPRIME
# Tienes 15 años, eres un adolescente
