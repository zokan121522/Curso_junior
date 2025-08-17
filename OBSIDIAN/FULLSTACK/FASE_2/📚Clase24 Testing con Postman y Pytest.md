## ✅ Qué debes ENTENDER (no memorizar)

- **Qué es cada pieza y dónde va:**

- **`main.py`** → Tu API (rutas, modelo, conexión BD).

- **`tests/conftest.py`** → Fixtures compartidas (BD en memoria, cliente de test).

- **`tests/test_api.py`** → Casos de prueba.

- **Flujo de un test** → Cliente → petición → `assert status_code` → `assert datos`.

- **Por qué BD en memoria** → Tests no tocan `tareas.db`.

- **Validación de datos** → 422 si título vacío, 404 si no existe.

  

Con eso claro, lo demás lo rellenas con **snippets** y luego ajustas nombres/rutas según el ejercicio.

---

## 🔹 Snippets que YA tienes (VS Code)

# 📌 Lista rápida de triggers (VS Code)

• fa-app-sql → main.py con API FastAPI + SQLModel + CRUD básico.

• fa-pytest-fixtures → conftest.py con BD en memoria + cliente de prueba.

• fa-tests-crud → Tests CRUD básicos (listar, crear, obtener, borrar).

• fa-tests-extra → Tests extra (422, 404, DELETE doble, done por defecto).

• fa-reqs → requirements.txt mínimo para FastAPI + Pytest.

• fa-pytest-ini → pytest.ini básico apuntando a carpeta tests.

• fa-curl-post → Comando curl para POST /tareas desde terminal.

  

*(Triggers y contenido están en `snipetsVscode.json`)*

  

---

  

## 🛠 Clase 24 — Paso a paso usando snippets

  

1. **Crea la API**

- Abre `main.py` vacío → escribe `fa-app-sql` → `TAB`.

- Modifica: nombre del modelo, campos extra, rutas si cambian.

  

2. **Prepara los tests (fixtures)**

- Crea `tests/conftest.py` → escribe `fa-pytest-fixtures` → `TAB`.

- Esto monta SQLite en memoria + cliente para pruebas limpias.

  

3. **Añade tests base**

- Crea `tests/test_api.py` → escribe `fa-tests-crud` → `TAB`.

- Para más casos: añade partes de `fa-tests-extra`.

  

4. **Instala dependencias**

```bash

mkidir requirements.txt

fastapi

uvicorn

sqlmodel

pytest

httpx

  

pip install -r requirements.txt

```

  

5. Ejecuta tests

```bash

pytest -q

• ✅ Verde = OK.
• ❌ Rojo = mensaje de error (ajusta ruta/modelo/status code).
```

```

Arrancamos el servidor con :

terminal → uvicorn main:app --reload

  

```

6. Tests manuales con Postman (opcional)

• POST → http://localhost:8000/tareas → body JSON:

```json

{ "titulo": "Aprender FastAPI", "done": false }

```

```bash

• GET → http://localhost:8000/tareas

• DELETE → http://localhost:8000/tareas/{id} → comprobar con GET.

```

---

  

## ✏️ Lo que SÍ debes saber modificar

• Rutas (/tareas, /tareas/{id}) si cambia el ejercicio.

• Modelo de datos (campos, tipos, validaciones min_length, valores por defecto).

• Códigos de estado (201 creado, 204 sin contenido, 404 no encontrado, 422 validación).

• Asserts en tests (lo que esperas recibir: JSON, campos, valores).

  

---

  
  

> 💡 Si cambias de “tareas” a “usuarios” o “productos”, solo ajustas el nombre en el snippet y en el modelo.

  

---

  

## ✅ Checklist de comprensión

1) ¿Qué hace fa-app-sql y qué tocas después?

• Qué genera: main.py con FastAPI + SQLModel, modelos (Tarea, TareaCreate), rutas (GET/POST/DELETE), engine SQLite.

• Qué debes tocar:

• Nombre del modelo y campos (Tarea → Usuario, añadir email, etc.).

• Validaciones (min_length, regex, default).

• Rutas (/tareas → /usuarios).

• Autotest rápido: Cambia titulo → nombre, ajusta tests y ejecuta pytest -q (debe seguir en verde).

---

2) fa-pytest-fixtures → BD en memoria + client

• Qué hace: Crea un engine en memoria con StaticPool, limpia tablas antes de cada test y expone client.

• Señales de que funciona:

• Tu archivo real tareas.db no cambia al correr tests.

• Cada test arranca “limpio” (la lista empieza vacía).

• Autotest rápido: Añade dos tareas en un test y en otro verifica que GET /tareas vuelve []. Si sale así, la BD de tests es independiente.

![alt text](image.png)

---

3) ¿Lees un test? petición → assert status_code → assert datos

• Patrón mental:

• resp = client.post("/tareas", json={...})

• assert resp.status_code == 201

• data = resp.json(); assert data["id"] is not None

• Autotest rápido: Cambia un assert a un valor incorrecto (ej. assert resp.status_code == 200) y comprueba que Pytest te muestra exactamente qué falló.

---

4) ¿Por qué 422 y 404?

• 422 (Unprocessable Entity): Validación de entrada falla (p. ej., titulo vacío con min_length=1).

• Probar: POST /tareas con {"titulo": ""} → debe dar 422.

&nbsp;

• 404 (Not Found): Pides/borras un recurso que no existe.

• Probar: GET /tareas/99999 o DELETE /tareas/99999 → debe dar 404.

---

5) Mini‑reto exprés (1 minuto cada uno)

• Cambia la ruta a /items y el campo titulo por nombre. Ajusta los tests → pytest -q.

• Añade descripcion: str | None = None en el modelo y verifica que aparece en el JSON.

• Haz que done por defecto sea True y cambia el test correspondiente.

• Lanza uvicorn main:app --reload y prueba en /docs un POST válido e inválido (mira 201 vs 422).

• Borra dos veces la misma id en Postman → 204 la primera, 404 la segunda.

---

> 💬 Si todo esto lo tienes claro, vas como un pro: no memorizas sintaxis, entiendes la lógica y usas snippets como herramienta de trabajo real.

  

## 🧪 Ejercicios prácticos de modificación — Clase 24

  

### 1. Cambiar el nombre del recurso

  

#### Objetivo: Practicar cómo adaptar modelo, rutas y tests.

• Cambia el modelo Tarea → Producto.

• Cambia las rutas /tareas → /productos.

• Ajusta los tests (fa-tests-crud y fa-tests-extra) para usar "nombre" en lugar de "titulo".

• Comprueba: Todos los tests deben seguir pasando (pytest -q).

  

---

  

### 2. Añadir un campo obligatorio nuevo

  

#### Objetivo: Usar validación Pydantic.

• Añade a TareaCreate un campo descripcion: Annotated[str, PydField(min_length=10)].

• Modifica el modelo Tarea para incluirlo.

• Cambia los tests para que envíen descripcion con al menos 10 caracteres.

• Comprueba: Si no lo envías o es muy corta, el test debe fallar con 422.

  

---

  

### 3. Cambiar valores por defecto y comprobar en tests

  

#### Objetivo: Entender valores por defecto y asserts.

• Cambia done: bool = False por done: bool = True en ambos modelos.

• Ajusta el test test_done_por_defecto_false para verificar que ahora es True.

• Comprueba: El test pasa si el valor por defecto es el nuevo.

  

---

  

### 4. Personalizar códigos de estado

  

#### Objetivo: Modificar respuestas HTTP.

• Cambia el código de respuesta de POST /tareas de 201 a 200.

• Cambia DELETE /tareas/{id} de 204 a 200 devolviendo un JSON como {"status": "deleted"}.

• Ajusta los tests para verificar estos nuevos códigos y respuesta.

• Comprueba: El cambio se refleja en verde al pasar los tests.

  

---

  

### 5. Simular un fallo en BD en memoria

  

#### Objetivo: Entender la función de fixture y la BD en memoria.

• En fa-pytest-fixtures, comenta la línea SQLModel.metadata.create_all(test_engine) y ejecuta los tests.

• Observa que ahora fallan porque no hay tablas.

• Descomenta la línea para restaurar el comportamiento.

• Comprueba: Los tests vuelven a pasar y entiendes por qué la BD en memoria es esencial.

  

---

  

> 📌 Recomendación:

Haz estos ejercicios uno por uno y ejecuta pytest -q tras cada cambio. Así verás exactamente qué parte rompe y por qué, reforzando la comprensión.

  

---

## 📚 Tabla de Conceptos — Clase 24 (Testing con Postman y Pytest, modo Snippets)

  

| 📌 Concepto | 📖 Explicación técnica | 💬 Explicación coloquial |

|-------------|-----------------------|--------------------------|

| ⚡ **FastAPI** | Framework moderno para construir APIs rápidas en Python. | 🏭 “La fábrica donde montamos nuestras rutas y lógica de API.” |

| 🗄 **SQLModel** | Combina SQLAlchemy + Pydantic para manejar BD y validación. | 🤝 “El ayudante que convierte tu clase en tabla de BD y valida datos.” |

| 🛡 **Pydantic** | Valida datos de entrada y salida en modelos. | 🚪 “El portero que no deja pasar datos incorrectos.” |

| 🚀 **Uvicorn** | Servidor ASGI rápido y ligero para ejecutar aplicaciones FastAPI. | ⚡ “El motor que arranca y mantiene viva la API.” |

| 🧪 **Pytest** | Framework de testing para Python. | 🕵️ “El inspector que revisa que todo funcione como debe.” |

| 🌐 **HTTPX** | Cliente HTTP compatible con async usado en tests. | 📬 “El cartero rápido que entrega y recibe cartas para pruebas.” |

| 🧠 **main.py** | Archivo principal con API, modelos y conexión BD. | 🗺 “El cerebro y plano de la API.” |

| 🌐 **Ruta (endpoint)** | URL + método HTTP que ejecuta una función. | 🚪 “La puerta que lleva a un sitio específico de la API.” |

| 📥 **Modelo de entrada** | Clase para definir cómo deben venir los datos de un POST. | 🛠 “El molde para que los datos lleguen con la forma correcta.” |

| 🔄 **Fixture (Pytest)** | Función que prepara recursos antes del test. | 📦 “El ritual que deja todo listo antes de probar.” |

| 🧰 **conftest.py** | Guarda fixtures compartidas para todos los tests. | 📦 “La caja de herramientas común.” |

| 📮 **TestClient** | Simula peticiones HTTP sin servidor real. | 📬 “El cartero falso que entrega cartas sin salir de casa.” |

| 🔗 **StaticPool** | Mantiene la misma conexión SQLite en memoria. | 🚪 “La puerta de la BD siempre abierta.” |

| 📝 **connect_args** | Ajustes extra para conexión BD. | 🗒 “Notas para que el motor BD trabaje como quieres.” |

| ⚙ **pytest.ini** | Configuración de Pytest. | 📜 “Las reglas del juego para Pytest.” |

| 🛒 **requirements.txt** | Lista de librerías necesarias. | 📋 “La lista de la compra para Python.” |

| 🚦 **status_code** | Código que indica resultado HTTP. | 🚥 “Semáforo: verde (200), creado (201), error (404)…” |

| 🔴 **422** | Datos inválidos. | 📦 “Paquete roto en la puerta.” |

| 🚫 **404** | Recurso no encontrado. | ❓ “Puerta inexistente.” |

| 🟢 **201** | Recurso creado correctamente. | 🪑 “Pusiste un mueble nuevo y quedó perfecto.” |

| ⚪ **204** | Acción OK pero sin contenido. | 📭 “Lo hiciste, pero no hay nada que mostrar.” |

| 🟢 **200** | Petición exitosa. | 📄 “Todo bien, aquí tienes lo que pediste.” |

| 🟠 **400** | Petición mal formada. | 📝 “Me pediste algo pero está mal escrito o incompleto.” |

| ✅ **assert** | Verifica que algo es cierto en el test. | 🗣 “Esto debería ser así… y si no, me quejo.” |

| 💾 **BD en memoria** | Base de datos temporal que vive en RAM. | 🗒 “Cuaderno que tiras después de la clase.” |

| 🔄 **CRUD** | Crear, Leer, Actualizar, Borrar. | 🛠 “Las 4 acciones básicas con cualquier cosa que guardes.” |

| 📬 **Postman** | App para probar APIs manualmente. | 🧪 “Probar puertas antes de invitar gente.” |

| 💻 **curl** | Comando para hacer peticiones HTTP. | 🕶 “Postman pero en modo hacker.” |

  
  

---

  

## 💻 CURL

  

#### 📤 Crear recurso (POST)

```bash

curl -X POST http://localhost:8000/tareas \

-H "Content-Type: application/json" \

-d '{"titulo": "Aprender FastAPI", "done": false}'

```

> 💡 Envía JSON para crear una tarea nueva.

  

&nbsp;

  

#### 📋 Listar recursos (GET)

```

curl http://localhost:8000/tareas

```

>💡 Obtiene todas las tareas.

  

&nbsp;

  

#### 🔍 Obtener por ID (GET)

```bash

curl http://localhost:8000/tareas/1

```

>💡 Devuelve la tarea con ID 1.

  

&nbsp;

  

#### 🗑 Borrar por ID (DELETE)

```bash

curl -X DELETE http://localhost:8000/tareas/1

```

>💡 Borra la tarea con ID 1.

  

&nbsp;

  

#### 🚫 Simular 422 (POST inválido)

```bash

curl -X POST http://localhost:8000/tareas \

-H "Content-Type: application/json" \

-d '{"titulo": ""}'

```

> 💡 Envía título vacío → deberías recibir 422.

  

&nbsp;

  

#### ❓ Simular 404 (GET inexistente)

```bash
curl http://localhost:8000/tareas/9999
```

> 💡 Pide un ID que no existe → deberías recibir 404.