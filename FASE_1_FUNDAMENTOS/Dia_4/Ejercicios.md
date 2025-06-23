
# 🔢 5 EJERCICIOS NUEVOS DE HOY (de menos a más)
```texto
🎯 OBJETIVO
¿Qué quiero lograr?
✏️ _____________________________________

📥 ENTRADA
¿Qué necesito pedir o usar?

✏️ _____________________________________

🧠 PASOS LÓGICOS
1. ___________________________________
2. ___________________________________
3. ___________________________________
```
## 🧾 FUNCIÓN EN PYTHON

```python
def nombre_funcion(parámetros):
    # Paso 1
    # Paso 2
    return resultado
```


## 1. Crear una lista con 3 frutas y mostrarlas una por una
```python
lista = ["manzana","sandia","pera"]

for fruta in lista:
    print("Eres una ", fruta)
```

## 2. Pedir 5 números al usuario y guardarlos en una lista

```python lista = []
for i in range(5):
    n = int(input(f"Dime un numero {i + 1}: ")) # 
    # en lista añade (n)
    lista.append(n)
```

## 3. Calcular el promedio de una lista de números
```python
numeros = [3,4,5]
promedio = sum(numeros)/len(numeros)
print(f"el promedio de {numeros} es", promedio)
```

## 4. Mostrar los elementos de una lista en orden inverso
```python
mochila = ["brujula","rejol","cartera"]
for n in reversed (mochila):
    print(n)
```

## 5. Dada una lista de edades, contar cuántos son mayores de edad (>=18)
```python
edades = [15, 22, 17, 19, 30]     # Lista con varias edades
contador = 0                      # Inicializa el contador en 0

for edad in edades:              # Recorre cada edad de la lista
    if edad >= 18:               # Si la edad es mayor o igual a 18...
        contador += 1            # ...suma 1 al contador

print("Mayores de edad:", contador)  # Muestra cuántos son mayores de edad
```



# 🔄 REPASO GLOBAL (Funciones + Condicionales + Listas + Bucle)

##  1. funcion crear\_lista() que pida 3 elementos por input y devuelva lista
```python
def crear_lista():                         
    lista = []                             
    for i in range(3):                    
        item = input(f"Introduce el elemento {i+1}: ")  
        lista.append(item)                 
    return lista    
```                      

## 2. funcion es par(n): devuelve True si n es par, usando return
```python
def es_par(n):                             
    return n % 2 == 0                     
```


##  3. funcion mayores(lista): recibe lista de edades y devuelve solo los >=18

```python
def mayores(lista):                        
    listaFiltrada = []                  # Aquí guardaremos solo los mayores de edad                        
    for edad in lista:                  # Recorremos cada edad en la lista original
        if edad >= 18:                  # Si es mayor o igual que 18...
            listaFiltrada.append(edad)  # ...la añadimos a la lista filtrada        
    return listaFiltrada                # Devolvemos solo los mayores   
```         


## 4. funcion contar\_aprobados(lista): cuenta notas >= 5
``` python
def contador(lista):
    contador = 0                   # 1. Crear contador en 0  
    for numero in lista:            # 2. Recorrer cada nota  
        if numero >= 5:            # 3. Si la nota es ≥ 5 → sumar 1  
            contador +=1
    return contador                # 4. Devolver el contador final

print(contador([4,8,2]))
```

## 5. funcion resumen(nombre,edad,lista\_compras): muestraperfil personalizado cn resumen d compra

```python
def resumen ():
    nombre = input ("Como te llamas? ")
    edad = input(f"Que edad tienes {nombre}? ") 
    nota = input (f"Que nota has sacado {nombre} ")
    
    resumen = f"Hola {nombre}, tienes {edad} años, y has sacado un {nota}."
    return resumen

print(resumen())
```

