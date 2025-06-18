# FUNCIONES

# 1. Duplicar(n) → Devuelve el doble
"""
def dubplica(n):
    return n * 2
print(dubplica(2))
"""

# 2. Mayor_de_dos(a, b) → Devuelve el mayor
"""
def mayor_de_dos(a,b):
    if a < b:
        return b
    elif a > b:
        return a
    
print(mayor_de_dos(7,3))
"""

# 3. Saludo_personalizado(nombre, edad) → Saludo distinto según edad
"""
def saludo (nombre,edad):
    if edad < 18:
        return f"{nombre} eres menor"
    else:
        return f"{nombre} eres mayor"
print(saludo("jaime",41))
"""
 
# 4. calcular_precio_total(precio, cantidad, iva=21) → Usa parámetro por defecto
"""
def calcular_precio_total(precio,cantidad,iva=21):
    subtotal = precio * cantidad
    total = subtotal *(1+iva/100)
    return total

print(calcular_precio_total(10,3))
"""

# ✅ Ejercicio 5 – Precio final con descuento 🧾
# Crea una función calcular_precio_con_descuento(precio_unitario, cantidad, descuento=10)
"""
def descuento (precio,cantidad,descuento=10):
    sub = precio * cantidad
    total = sub * (1 - descuento/100)
    return total

print(descuento(2,2))
"""

# ✅ Ejercicio 6 – Tiempo total de viaje 🚗
"""
Crea una función tiempo_viaje(distancia_km, velocidad_kmh=100)
	•	Calcula el tiempo total del viaje (fórmula: distancia / velocidad)
	•	Devuelve el tiempo en horas
"""
# Primero logica luego codigo
"""
## 1. Objetivo
     Calcular las horas totales del viaje

## 2. Datos de entrada
    1. Kilometros totales
    2. Velocidad
    3. Horas

## 3. Pasos logicos mentales
    1. Saber distancia
    2. Saber velocidad
    3. Divido kilometros totales entre la velocidad y retornará el tiempo
    4. Imprimo el tiempo
"""

"""
def calcular_tiempo(kilometros,kilometros_hora):
    return kilometros /kilometros_hora
    
print(calcular_tiempo(200,100))
"""


"""
✅ Ejercicio 7 – Calcular nota final de examen 📚

Crea una función nota_final(examen, trabajo, extra=0)
	•	La nota final se calcula como:
examen * 0.6 + trabajo * 0.4 + extra
	•	El parámetro extra es opcional (por defecto 0)
	•	Devuelve la nota final total (puede pasar de 10)
"""

def calcular (examen, trabajo, extra=0):
    nota_final = examen * 0.6 + trabajo * 0.4 + extra
    return nota_final
print(calcular(5,5,1))