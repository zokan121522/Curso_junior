"""
- Pide nombre y edad.
- Calcula si es mayor de edad.
- Guarda los datos en una lista de diccionarios.

Analogía: Es como tu libreta de contactos: cada persona es un diccionario.

"""
nombre = input("Nombre: ")
edad = int(input("Edad: "))

if edad >=18:
    print(f"{nombre} eres mayor de edad")
else:
    print(f"{nombre} eres menor de edad")

agenda = []

ficha = {
    "nobre" : nombre,
    "edad" : edad
}

agenda.append(ficha)
print("\n\nFICHA TECNICA")
print("____________________\n")
print("Nombre: ",nombre,"\nEdad: ",edad)