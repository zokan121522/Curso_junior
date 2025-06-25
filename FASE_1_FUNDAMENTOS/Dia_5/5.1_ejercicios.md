
# 🧠 DÍA 5 – LÓGICA APLICADA CON FUNCIONES (IMC, Año Nacimiento)

---

## ✅ EJERCICIO 1: Calcular el IMC (Índice de Masa Corporal)

### 🎯 OBJETIVO
```
Calcular el IMC a partir del peso y altura de una persona y clasificar el resultado.
```
### 📥 ENTRADA
```
Pedir al usuario su peso (kg) y altura (m).
```
### 🧠 PASOS LÓGICOS
```
1. Pedir el peso y la altura con `input()`
2. Aplicar la fórmula: IMC = peso / (altura ** 2)
3. Clasificar según el valor obtenido
```
```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)  # Fórmula del IMC
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

peso = float(input("¿Cuál es tu peso en kg? "))
altura = float(input("¿Cuál es tu altura en metros? "))
resultado = calcular_imc(peso, altura)
print("✅ Tu clasificación IMC es:", resultado)
```
```
🧠 Frase para recordar: “Tu cuerpo es como un coche: el IMC te dice si va ligero, equilibrado o con sobrecarga.”
```

## ✅ EJERCICIO 2: Calcular año de nacimiento

### 🎯 OBJETIVO
```
Saber en qué año nació una persona usando su edad actual.
```
### 📥 ENTRADA
```
Pedir la edad actual al usuario.
```
### 🧠 PASOS LÓGICOS
	1.	Obtener la edad actual
	2.	Obtener el año actual del sistema (usando datetime)
	3.	Restar edad al año actual

```python
from datetime import datetime

def calcular_nacimiento(edad):
    actual = datetime.now().year  # Año actual del sistema
    return actual - edad  # Año estimado de nacimiento

edad = int(input("¿Cuántos años tienes? "))
nacimiento = calcular_nacimiento(edad)
print("🎂 Naciste en el año:", nacimiento)

```


## ✅ EJERCICIO 3: Clasificar temperatura

### 🎯 OBJETIVO
```
Decidir si hace frío, calor o está templado según la temperatura.
```
### 📥 ENTRADA
```
Temperatura en grados Celsius.
```
### 🧠 PASOS LÓGICOS
	1.	Pedir temperatura
	2.	Evaluar rangos con condicionales
	3.	Mostrar categoría

```python
def clasificar_temperatura(temp):
    if temp < 10:
        return "❄️ Hace frío"
    elif temp <= 25:
        return "🌤️ Temperatura agradable"
    else:
        return "🔥 Hace calor"

temp = float(input("¿Qué temperatura hace hoy? "))
print(clasificar_temperatura(temp))
```


## ✅ EJERCICIO 4: Verificar si una palabra es palíndromo

### 🎯 OBJETIVO
```
Comprobar si una palabra se lee igual al derecho y al revés.
```
### 📥 ENTRADA
```
Pedir una palabra.
```
### 🧠 PASOS LÓGICOS
	1.	Pedir palabra
	2.	Compararla con su reverso ([::-1])
	3.	Devolver True o False
```python 
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  # Normalizamos
    return palabra == palabra[::-1]  # Comparamos con versión invertida

texto = input("Escribe una palabra: ")
if es_palindromo(texto):
    print("✅ Es un palíndromo.")
else:
    print("❌ No es un palíndromo.")
```

## ✅ EJERCICIO 5: Validar contraseña

### 🎯 OBJETIVO
```
Verificar si la contraseña cumple ciertas condiciones.
```
### 📥 ENTRADA

```
Pedir contraseña al usuario.
```


### 🧠 PASOS LÓGICOS
	1.	Comprobar que tiene al menos 8 caracteres
	2.	Que incluya números y letras
	3.	Validar todo junto

```python

def validar_contraseña(clave):
    return (
        len(clave) >= 8 and
        any(c.isdigit() for c in clave) and
        any(c.isalpha() for c in clave)
    )

clave = input("Introduce tu contraseña: ")
if validar_contraseña(clave):
    print("🔐 Contraseña válida.")
else:
    print("❌ Contraseña inválida. Mínimo 8 caracteres, letras y números.")
```
