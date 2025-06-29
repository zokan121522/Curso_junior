# 🧠 DÍA 9 – MAQUETACIÓN WEB SIMPLE

## ✅ ENUNCIADO DETALLADO – PASO A PASO

### 📌 1. Crea la estructura de tu proyecto
```bash

- Abre VSCode y dentro de tu carpeta de trabajo crea una carpeta llamada **dia_9_web_personal**.
- Dentro de esta carpeta, crea:
  - Un archivo **index.html**
  - Un archivo **style.css**
  - Una carpeta **assets/** y coloca dentro una imagen tuya o de prueba.
```
---

### 📌 2. Diseña la estructura base en HTML
``` bash
- Abre **index.html** y escribe la estructura base:
  - Usa `<!DOCTYPE html>` para definir HTML5.
  - Abre las etiquetas `<html>`, `<head>` y `<body>`.
- Dentro de `<head>`, añade:
  - `<meta charset="UTF-8">` para caracteres especiales.
  - `<title>` con el nombre de tu web.
  - `<link rel="stylesheet" href="style.css">` para enlazar tu CSS.
```
---

### 📌 3. Maqueta el contenido principal
```bash
- Dentro de `<body>`, crea:
  - Un `<header>` con tu nombre usando `<h1>`.
  - Una `<section>` con `class="contenido"`:
    - Inserta una imagen (`<img>`) apuntando a tu archivo dentro de **assets/**.
    - Escribe un `<p>` con una breve descripción sobre ti: quién eres, qué estudias o qué te interesa.
  - Un `<footer>` que muestre el año actual y un mensaje como "Todos los derechos reservados".
```
---

### 📌 4. Crea el archivo CSS básico
```bash
- Abre **style.css** y agrega reglas básicas para:
  - Configurar la fuente de toda la página (sans-serif).
  - Cambiar el color de fondo del `<body>`.
  - Centrar todos los textos.
  - Aplicar un color de fondo oscuro y texto blanco al `<header>`.
  - Hacer la imagen circular con `border-radius: 50%`.
  - Agregar márgenes para separar las secciones.
```
---

### 📌 5. Organiza todo en carpetas
```bash

- Verifica que tu estructura de carpetas se vea así:

dia_9_web_personal/
│
├── index.html
├── style.css
├── assets/
│   └── foto.jpg
```
---

### 📌 6. Inicializa Git y sube a GitHub
```bash
- Abre la terminal en VSCode dentro de la carpeta del proyecto:
  - Ejecuta `git init` para inicializar Git.
  - Añade todos los archivos: `git add .`
  - Haz commit: `git commit -m "Web personal Día 9"`
  - Crea un repositorio vacío en GitHub.
  - Conecta tu repositorio local con:  
    `git remote add origin <URL_DE_TU_REPO>`
  - Sube los cambios:  
    `git push -u origin main`
```
---

### ✅ Resultado final
```bash
Tu web debe verse así:
- Nombre en `<header>`, estilizado.
- Imagen redonda y descripción centrada.
- Footer discreto.
- CSS limpio enlazado.
- Proyecto organizado y subido a GitHub.
```
---

## 🧠 FRASE PARA RECORDAR

```bash
“Una web bien maquetada es como una buena carta de presentación: ordenada, clara y con estilo.”
```

