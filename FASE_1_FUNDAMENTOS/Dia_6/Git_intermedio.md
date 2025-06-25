
# 🧠 DÍA 6 – GIT INTERMEDIO: RAMAS, MERGE Y CONFLICTOS

---

## 🎯 Objetivo del día

- Entender qué es una **rama (branch)** en Git
- Crear, cambiar y fusionar ramas (**gitbranch**, **checkout**, **merge**`)
- Resolver conflictos cuando dos ramas modifican lo mismo
- Aplicar todo con práctica real sobre tu script **perfil.py**

---

## 🧩 ¿Qué es una rama en Git?

> **Analogía:** Imagina que estás escribiendo un libro.  
> Para probar una nueva idea, no borras el original: haces una **copia aparte** y pruebas allí. Eso es una **rama**.

```bash
main  ← línea principal (oficial)
│
├── experimento  ← una nueva idea, o funcionalidad en desarrollo
```

---

## ✨ COMANDOS BÁSICOS DE RAMAS EN GIT

| Acción                     | Comando                                  |
|----------------------------|------------------------------------------|
| Ver ramas existentes       | `git branch`                             |
| Crear nueva rama           | `git branch experimento`                 |
| Cambiar de rama            | `git checkout experimento`              |
| Crear y cambiar a la vez   | `git checkout -b experimento`           |
| Volver a **main**            | `git checkout main`                      |
| Fusionar rama con main     | `git merge experimento`                  |
| Borrar rama                | `git branch -d experimento`              |

---

## 📦 EJEMPLO GUIADO PASO A PASO

```bash
cd ruta/de/tu/proyecto
git init
git add perfil.py
git commit -m "Versión inicial de perfil"
```

## ✅ 1. Crear una rama nueva

```bash
git checkout -b experimento
```

```python
# perfil.py (modificación en rama experimento)
print("Hola, soy la versión experimental.")
```

## ✅ 2. Hacer commit en la rama

```bash
git add perfil.py
git commit -m "Cambios en rama experimento"
```

## ✅ 3. Volver a main y fusionar

```bash
git checkout main
git merge experimento
```

---

## ⚔️ ¿Qué es un conflicto en Git?

> **Analogía:** Dos personas editan el mismo párrafo de un documento.  
> Git se queda bloqueado y **te pide decidir**.

### ⚠️ Ejemplo de conflicto

```python
<<<<<<< HEAD
print("Hola, soy el original.")
=======
print("Hola, soy la nueva versión.")
>>>>>>> experimento
```

🛠️ Eliminas los símbolos y decides:

```python
print("Hola, soy la nueva versión.")
```

```bash
git add perfil.py
git commit -m "Resuelto conflicto"
```

---

## 🧪 RETO GUIADO

1. Crear rama **experimento**
2. Hacer cambios en **perfil.py**
3. Simular conflicto modificando lo mismo en **main**
4. Hacer merge y resolverlo manualmente

---

## ✅ 5 EJERCICIOS INTERACTIVOS

1. Crear rama **feature-x**, editar **perfil.py**, volver a main
2. Fusionar **feature-x** en **main** sin conflicto
3. Crear conflicto modificando misma línea en ambas ramas
4. Resolver conflicto y hacer commit de fusión
5. Crear 2 ramas hijas y fusionarlas antes de volver a **main**

---

## 🧠 FRASE PARA RECORDAR

> “Una rama en Git es como un laboratorio: pruebas sin romper nada.  
> Un conflicto es solo una decisión pendiente.”
