# perfil.py

"""
Aquí aprenderás:
- Cómo leer entrada del usuario con input()
- Convertir strings a números (int, float)
- Formatear el texto de salida
"""

print(" Bienvenido, vamos a crear tu perfil:")

nombre = input("¿Como te llamas?")
edad = int(input("¿Que edad tienes?"))
ciudad = input("¿En que ciudad vives?")

print("/n✅  Perfil generado:")
print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")


