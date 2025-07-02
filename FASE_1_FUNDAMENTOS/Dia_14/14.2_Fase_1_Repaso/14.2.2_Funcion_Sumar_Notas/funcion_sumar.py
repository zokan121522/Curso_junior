"""
• Lista de notas (ej: [7, 5, 8, 9]).
• Recorre con for.
• Calcula promedio usando función.

Analogía: Es como sumar las facturas del mes y sacar la media.
"""

lista = [7, 5, 8, 9]

def CalcularPromedio (lista_notas):
    return sum (lista_notas) / len(lista_notas)

promedio = CalcularPromedio(lista)

print("Promedio es: ",promedio)