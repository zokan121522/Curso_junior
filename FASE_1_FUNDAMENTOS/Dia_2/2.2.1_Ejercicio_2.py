# Ejercicio_2.py

"""
Crea un sistema básico de login que:
- Pida al usuario su nombre de usuario y contraseña por consola.
- Verifique si ambos coinciden con las credenciales:
    - Usuario: "admin"
    - Contraseña: "1234"
- Si son correctos, imprime "✅ Acceso permitido"
- Si no, muestra "🚫 Usuario o contraseña incorrectos"
💡 Usa condiciones con and para validar ambos campos a la vez.
"""

usuario = input("Nombre de usuario: ")
contraseña = input ("Contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("✅ Acceso permitido")
else:
    print("🚫 Usuario o contraseña incorrectos")
