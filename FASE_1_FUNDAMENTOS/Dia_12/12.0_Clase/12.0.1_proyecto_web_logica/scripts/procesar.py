# procesar.py

valoracion = int(input("Valoracion del 1 al 5: "))
comentarios = input("Comentarios: ")

if valoracion >= 4:
    print("Gracias por tu valoración positiva.")
elif valoracion == 3:
    print("Gracias, mejoraremos para subir esa nota.")
else:
    print("Sentimos no haber cumplido tus expectativas.")

