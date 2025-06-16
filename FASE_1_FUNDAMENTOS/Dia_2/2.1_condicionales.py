# condicionales.py

nombre = input("Como te llamas? ")
edad = int(input("Que edad tienes ? "))

"""if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print(f"Hola {nombre} tienes {edad}")
"""

if edad <= 12:
    print("Eres un niño")
elif edad > 18:
    print("Eres un adolescente.")
else:
    print("Eres adulto")


