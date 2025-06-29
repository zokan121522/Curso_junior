# Creo diccionario con datos
perfil = {
    "nombre": "Zokan",   # nombre clave:valor
    "edad": 34,          # edad clave:valor
    "ciudad": "Barcelona" # ciudad clave:valor
}

print("Claves:") # Titulo

for clave in perfil.keys():
    print(clave)
# Analogía: cada clave es como el nombre de una casilla

# Muestro valores
print("\nValores:")
for valor in perfil.values():
    print(valor)
# Analogía: cada valor es lo que hay guardado en la casilla