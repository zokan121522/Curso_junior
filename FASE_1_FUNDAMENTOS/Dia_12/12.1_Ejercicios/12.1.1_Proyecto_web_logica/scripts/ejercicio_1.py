usuario = input("Nombre de usuario: ")
email = input("Email: ")
edad = int(input("Edad: "))

if edad < 18:
    print(f"{usuario} eres menor de edad")
else:
    print(f"{usuario} eres mayor de edad")