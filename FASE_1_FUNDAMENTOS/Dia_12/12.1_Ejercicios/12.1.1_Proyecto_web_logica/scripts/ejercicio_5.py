"""
Qué pide:
• Usuario
• Contraseña
✔ Lógica:
Si usuario == admin y clave == 1234 → “Acceso permitido.”
Si no → “Usuario o contraseña incorrectos.”
"""

nombre = input("Usuario: ")
contraseña = int(input("Contraseña: "))

if nombre == "admin" and contraseña == 1234:
    print("Acceso permitido")
else:
    print("Usuario o contraseña incorrectos")