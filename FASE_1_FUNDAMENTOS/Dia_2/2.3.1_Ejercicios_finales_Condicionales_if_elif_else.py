# if / elif / else

"""
✅ Reto 1 – Control de acceso
> Pide al usuario su edad.
> Si es menor de 13: dile que no puede entrar.
> Si tiene entre 13 y 17: entra con supervisión.
> Si tiene 18 o más: entra libremente.
"""

"""
edad = int(input("Que edad tienes ? "))
if edad < 13:
    print("tiene menos de 13 años, no puedes entrar")
elif edad < 18:
    print("eres mayor de 13 pero menos de 18, entra con supervisión")
else:
    print("eres mayor de edad, puedes entrar libremente")
"""
#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#

"""
✅ Reto 2 – Termómetro humano
> Según una variable temperatura, muestra:
- “Congelado ❄️” si está por debajo de 0
- “Fresco 🧥” si está entre 0 y 20
- “Caliente ☀️” si pasa de 20
"""
"""
temperatura = int(input("Que temperatura hace ? "))
if temperatura < 0:
    print("Congelado ❄️")
elif temperatura <= 20:
    print("Fresco 🧥")
else:
    print("Caliente ☀️")
"""

#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#

"""
✅ Reto 3 – Semáforo
> Según el color de una variable semaforo:
- Si es “rojo”, imprime “Detente”
- Si es “amarillo”, “Prepárate”
- Si es “verde”, “¡Adelante!”
- Si es otro, “Color no válido”
"""
"""
semaforo = input("De que color está el semaforo?")
if semaforo == "rojo":
    print("Detente")
elif semaforo == "amarillo":
    print("Prepárate")
elif semaforo == "verde":
    print("¡Adelante!")
else:
    print("Color no válido")
"""


#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#

"""
✅ Reto 4 – Adivina la nota
> Dada una nota numérica del 0 al 10:
- < 5: “Suspenso”
- 5 a 6: “Aprobado”
- 7 a 8: “Notable”
- 9 a 10: “Sobresaliente”
"""
"""
nota = int(input("Adivina la nota? "))
if nota < 5:
    print("Suspenso")
elif nota <= 6:
    print("Aprobado")
elif nota <= 8:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")
else:
    print("Introduce otra vez el dato...")
"""


#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
"""
✅ Reto 5 – Calculadora de energía
> Según una variable fruta, muestra cuántas calorías tiene:
- Manzana: 52
- Plátano: 89
- Naranja: 47
- Si no es ninguna de esas, “Fruta no registrada”
"""


"""
fruta = input("Elige entre manzana,platano y naranja y te diré cuantas calorias tiene...")
if fruta == "manzana":
    print("52 calorias")
elif fruta == "plantano":
    print("89 calorias")
elif fruta == "naranja":
    print("47 calorias")
else:
    print("Fruta no registrada")
"""