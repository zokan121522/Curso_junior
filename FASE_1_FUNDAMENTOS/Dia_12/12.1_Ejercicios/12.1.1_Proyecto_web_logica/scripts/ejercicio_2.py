valoracion = int(input("Dime un numero del 0 al 5: "))
comentario = (input("Dime un comentario: "))

if valoracion >=4:
    print(f"Gracias por el feedback: {comentario}")
elif valoracion ==3:
    print(f"Lamento que no esté a tu gusto dime como mejorarlo: {comentario}")
else:
    print(f"Mejoraremos a la proxima! y gracias por: {comentario}")

