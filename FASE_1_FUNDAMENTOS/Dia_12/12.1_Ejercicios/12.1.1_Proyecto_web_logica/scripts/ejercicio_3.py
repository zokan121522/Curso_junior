"""
Qué pide:
    • Año de nacimiento
✔ Lógica:
    Calcular edad actual y mostrar:
    • <18 → “Necesitas supervi
"""
nacimiento = int(input("Año de nacimiento: "))

edad = 2025 - nacimiento

if edad <18:
    print("Necesitas supervisión")
else:
    print("Puedes pasar")
    