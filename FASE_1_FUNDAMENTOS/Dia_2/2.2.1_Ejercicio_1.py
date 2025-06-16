# Ejercicio_1.py

"""
🧪 Mini-reto 1: Actualiza perfil.py con validación de edad
Objetivo:
Mejora tu archivo perfil.py para que, además de pedir los datos básicos (nombre, edad, ciudad),
también incluya una validación condicional según la edad del usuario.

Requisitos:
	1.	Muestra un mensaje inicial indicando que se está creando el perfil.

	2.	Solicita al usuario:
	    •	Su nombre
	    •	Su edad
	    •	Su ciudad

	3.	Muestra un resumen del perfil del usuario.

	4.	Añade una lógica condicional:
	    •	Si el usuario es menor de 18 años, mostrar que es menor de edad.
	    •	Si tiene entre 18 y 64, mostrar que tiene acceso completo.
	    •	Si tiene 65 o más, mostrar que tiene acceso con modo lectura ampliada.
"""
print("Creando perfil...")

nombre = input("Como te llamas? ")
edad = int(input("Que edad tienes? "))
ciudad = input("De donde eres? ")

print("Ficha tecnica")
print(f"Nombre de usuario:  {nombre}")
print(f"La edad de {nombre} es de {edad} años de edad")
print(f"{nombre} que tiene {edad} años vive en {ciudad}")

if edad < 18:
    print(f"El usuario {nombre} tiene {edad} años, por ende es menor de edad")
elif edad < 64:
    print(f"El usuario {nombre} tiene {edad} años, tiene acceso completo")
elif edad < 65:
    print(f"El usuario {nombre} tiene {edad} años, por lo tanto tiene acceso con modo lectura ampliada")
else:
    print("Dato incorrecto, vuelve a marcarlo...")

