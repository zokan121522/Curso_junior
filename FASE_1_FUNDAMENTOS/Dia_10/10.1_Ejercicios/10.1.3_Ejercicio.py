# Pedir datos 2 veces y guardar cada perfil en lista.

usuiarios = []

for i in range(2):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    perfil = {
        "Nombre" : nombre,
        "Edad" : edad,
        "Ciudad" : ciudad
    }

    usuiarios.append(perfil)

print("Perfiles Guardados")

for usuario in usuiarios:
    print("Percil Creado: \n\n")
    print("\nNombre: ",perfil["Nombre"],"\nEdad:",perfil["Edad"],"\nCiudad",perfil["Ciudad"])

