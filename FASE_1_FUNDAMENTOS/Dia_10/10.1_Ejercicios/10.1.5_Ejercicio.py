# Contar cuántos perfiles tienen edad >= 18.

usuarios = [
    {"nombre" : "Jaime", "edad" : 41},
    {"nombre" : "Jesica", "edad" : 39},
    {"nombre" : "Ian", "edad" : 13},
    {"nombre" : "Zoe", "edad" : 10},
    {"nombre" : "Kai", "edad" : 2}
]

contador = 0

for usuario in usuarios:
    if usuario["edad"] <= 18:
        contador += 1

print ("La cantidad de menores es de: ",contador)