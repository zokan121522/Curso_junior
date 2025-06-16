# 2.3.2_Ejercicios_finales_Operadores_Logicos_or_not

# ✅ Ejercicio 1 – Entrada al parque temático 🎢
"""
Pide la edad y estatura de una persona.
Permitir la entrada si:
    - Tiene más de 12 años **o** mide más de 1.50 m
    - Si no cumple ninguna, mostrar mensaje de rechazo.
"""
# CODIGO
"""
edad = int(input("Que edad tienes? "))
altura = float(input("Cuanto mide? "))

if edad > 12 or altura > 1.5 :
    print("Puedes entrar ✅")
else:
    print("No puedes entrar ")
"""


# ✅ Ejercicio 2 – Clasificador de clima ☁️🌡️
"""
Según la temperatura ingresada:
    - < 5: “Frío extremo”
    - 5–15: “Frío”
    - 16–25: “Agradable”
    - 25: “Calor”
    - Si se ingresa un número negativo: “Temperatura no válida”
"""
# CODIGO
"""
temperatura = int(input("Ingresa la temperatura; "))
if temperatura < 5:
    print("frio extremo")
elif temperatura < 15:
    print("frio")
elif temperatura < 25:
    print("Temperatura agradable")
elif temperatura == 25:
    print("Calor")
else:
    print("Temperatura no válida")
"""


# ✅ Ejercicio 3 – Acceso a zona restringida 🔐
"""
El usuario solo puede pasar si su rol es "admin" **y** tiene clave correcta ("secreto123").
    Si no es admin, dile que no tiene permisos.
    Si es admin pero se equivoca con la clave, dile que revise su contraseña.
"""
# CODIGO
"""
usuario = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")

if usuario == "admin" and contraseña == "secreto123":
    print(f"Hola {usuario} contraseña correcta puedes pasar")
elif usuario == "admin" and not  contraseña == "secreto123":
    print (f"Hola {usuario} tu contraseña no es correcta")
elif usuario != "usuario":
    print("Nombre de usuario incorrecto")
"""


# ✅ Ejercicio 4 – Validación de nombre de usuario 📛
"""
Pide un nombre de usuario.
    Si está vacío o solo contiene espacios, mostrar: "Nombre inválido".
    Si el nombre es "admin" o "root", mostrar: "Nombre reservado".
    En cualquier otro caso, aceptar el nombre.
"""
# CODIGO
"""
nombre = input("Nombre de usuario: ")
if nombre == "":
    print("Nombre inválido")
elif nombre == "admin" or nombre == "root":
    print("Nombre reservado")
else:
    print("Nombre aceptado")
"""


# ✅ Ejercicio 5 – Alarma de seguridad 🚨
"""
Detecta si hay alguna alerta de peligro:
- Si movimiento_detectado **o** puerta_abierta es True, mostrar "¡Alarma activada!".
- Si not se cumple (ningún evento ocurre), mostrar "Zona segura".
"""
# CODIGO
"""
puerta_abierta = input("está la puerta abierta (si/no)? ")
movimiento_detectado = input("hay movimiento (si/no)? ")

if puerta_abierta == "si" or movimiento_detectado == "si":
    print("ALARMA ACTIVADA")
else:
    print("ZONA SEGURA")
"""