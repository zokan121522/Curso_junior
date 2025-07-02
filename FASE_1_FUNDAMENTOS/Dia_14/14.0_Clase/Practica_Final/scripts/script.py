carpeta =[]

nombre = input("Nombre: ")
edad = int(input("Edad: "))
ciudad = input("Ciudad: ")
estudios = input("Estudios: ")
trabajo = input("Trabajo: ")

ficha = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad,
    "estudios": estudios,
    "trabajo": trabajo,
}

carpeta.append(ficha)


print("Ficha Tecnica")
print("\n nombre: ",nombre,"\n edad: ",edad,"\n ciudad: ",ciudad,"\n estudios: ",estudios,"\n trabajo: ",trabajo)

if edad < 18:
    print(f"\n\n Hola {nombre} \n Si tienes {edad} años porque estas trabajando en {trabajo} ? \n Sigue desarrollando tus estudios en {estudios} ")
else:
    print(f"\n\n Hola {nombre} tienes {edad} años \n puedes seguir trabajando en {trabajo} \n pero acuerdate de seguir estudiando en {estudios}")