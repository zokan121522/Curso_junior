# perfil_tecnico.py
"""
- Cómo leer entrada del usuario con input()
- Convertir strings a números (int, float)
- Formatear el texto de salida
"""

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿En qué ciudad vives? ")


print("RESUMEN DEL PERFIL")
print("-" * 30)
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad:  {ciudad}")

# calculadora_años.py
"""
✅ Mini-reto (nivel 1)
Agrega al script perfil.py la capacidad de calcular tu año 
de nacimiento, suponiendo que estamos en 2025.
"""

año_nacimiento = 2025 - edad
print(f"Naciste en {año_nacimiento}")
