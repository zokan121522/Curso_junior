# 🧠 PLANTILLA UNIVERSAL – Recorrer, evaluar y hacer algo
```
🎯 ¿QUÉ QUIERO HACER?
Recorrer una lista y aplicar una acción **solo si** se cumple una condición.
```
---

## 🧩 ELEMENTOS CLAVE

| Parte       | Función                                                                 |
|-------------|-------------------------------------------------------------------------|
| `lista`     | Contenedor de datos a recorrer (`[1, 2, 3]`, `["hola", ...]`)           |
| `for`       | Recorre cada elemento uno por uno (`for x in lista:`)                   |
| `if`        | Evalúa una condición (`if x cumple algo:`)                              |
| Acción      | Lo que haces si se cumple (`sumar`, `contar`, `mostrar`, etc.)          |
| Resultado   | Variable que acumula, filtra o cuenta (`total`, `resultado`, `nuevo[]`) |

---

## 🗺️ PASOS LÓGICOS

```
1. Crear lista de datos  
2. Crear variable acumuladora (opcional)  
3. Usar `for` para recorrer  
4. Usar `if` para filtrar según condición  
5. Aplicar acción si se cumple  
6. Mostrar o devolver el resultado final
```
---

## 🔤 PSEUDOCÓDIGO
```
- “Por cada elemento en la lista…”
- “Si cumple la condición…”
- “Entonces hago algo con él”
```
---

## 🧾 PLANTILLA DE CÓDIGO

```python
datos = [elemento1, elemento2, ...]
resultado = valor_inicial  # Ej: 0, [], "", etc.

for item in datos:
    if condición_sobre(item):
        resultado = resultado + / modificar / guardar / contar

print(resultado)
```


## 🧪 EJEMPLOS DE APLICACIÓN

### ✅ 1. Contar
```python
numeros = [3, 7, 2, 9, 4]
contador = 0
for n in numeros:
    if n > 5:
        contador += 1
print("Mayores que 5:", contador)
```
### ✅ 2. Sumar
```python
numeros = [1, 2, 3, 4, 5, 6]
total = 0
for n in numeros:
    if n % 2 == 0:
        total += n
print("Suma de pares:", total)
```
### ✅ 3. Filtrar
```python
palabras = ["hola", "python", "es", "genial"]
largas = []
for palabra in palabras:
    if len(palabra) > 4:
        largas.append(palabra)
print("Palabras largas:", largas)
```

---
```
🧠 RECUERDA: Esta estructura se adapta a mil usos: contar, filtrar, transformar, verificar, etc.
```