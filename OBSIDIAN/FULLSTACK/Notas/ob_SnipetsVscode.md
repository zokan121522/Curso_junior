

# 📋 Tabla organizada por rutas y tipos

| 🖥 Lenguaje | 🚀 Framework | 📦 Librería(s)     | 📂 Ruta                         | 📂 Tipo de snippet | 🏷 Nombre snippet          | 💡 Qué hace                                                                       | 🧠 Concepto clave                                              | ✏️ Qué modificar tú                                        | 📄 Archivo                  |
| ----------- | ------------ | ------------------ | ------------------------------- | ------------------ | -------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| Python      | FastAPI      | SQLModel, Pydantic | `snippets/python_template.json` | Plantilla completa | **tpl-fa-app-sql**         | Crea API **FastAPI + SQLModel** con CRUD `Tarea` y validación de entrada.         | CRUD + validación (`min_length`), uso de `Session`/`SQLModel`. | Modelo (`Tarea`), campos, rutas (`/tareas`), validaciones. | `main.py`                   |
| Python      | Pytest       | FastAPI, SQLModel  | `snippets/python_module.json`   | Módulo/fixture     | **mod-pytest-fixtures**    | Configura **Pytest** con SQLite en memoria y `TestClient`.                        | Fixtures, `StaticPool`, `connect_args`.                        | Engine de test, fixture `client`.                          | `tests/conftest.py`         |
| Python      | Pytest       | FastAPI            | `snippets/python_module.json`   | Módulo (tests)     | **mod-tests-crud**         | Tests CRUD: listar, crear, obtener, borrar.                                       | TestClient + asserts.                                          | Endpoints y payloads; valores esperados.                   | `tests/test_api.py`         |
| Python      | Pytest       | FastAPI            | `snippets/python_module.json`   | Módulo (tests)     | **mod-tests-extra**        | Tests extra: 422 título vacío, 404 inexistente, DELETE doble, `done` por defecto. | Validaciones y errores HTTP.                                   | Reglas de validación, códigos esperados.                   | `tests/test_api.py`         |
| Texto plano | —            | —                  | `snippets/python_module.json`   | Módulo utilitario  | **mod-reqs**               | `requirements.txt` mínimo para API + tests.                                       | Dependencias base.                                             | Añadir/quitar libs.                                        | `requirements.txt`          |
| Texto plano | —            | Pytest             | `snippets/python_module.json`   | Módulo utilitario  | **mod-pytest-ini**         | `pytest.ini` apuntando a `tests/`.                                                | Config de descubrimiento de tests.                             | Cambiar `testpaths` si procede.                            | `pytest.ini`                |
| Bash        | —            | curl               | `snippets/bash_module.json`     | Módulo utilitario  | **mod-curl-post**          | Comando `curl` para POST `/tareas`.                                               | Probar sin Postman.                                            | URL/ruta/body JSON.                                        | —                           |
| JavaScript  | React        | —                  | `snippets/react.json`           | Función fetch      | **fetch-loadTareas**       | Cargar tareas desde API FastAPI.                                                  | `.fetch()`, estado.                                            | Endpoint.                                                  | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | Condicional JSX    | **fetch-condicional-done** | Mostrar “Hecho” o “Pendiente” con ternario.                                       | `tarea.done ?`                                                 | Texto a mostrar.                                           | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | Hook `useEffect`   | **useEffect-load**         | Ejecutar `loadTareas()` al montar.                                                | Hook de ciclo de vida.                                         | Función a ejecutar.                                        | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | Estado React       | **loading-state**          | Estado para mostrar "cargando...".                                                | `useState` + booleano.                                         | Nombre del estado.                                         | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | Carga condicional  | **loader-condicional**     | Mostrar tareas o loader.                                                          | `ternario` + `map()`.                                          | Nombre de estados y arrays.                                | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | Botón React        | **boton-refresh**          | Botón para recargar tareas.                                                       | `onClick`, diseño Tailwind.                                    | Función `handleRefresh`.                                   | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | `map()` con lista  | **map-lista**              | Iterar lista y renderizar `<li>`.                                                 | `map()` + `key`.                                               | Nombre del array y propiedades.                            | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | Hook reutilizable  | **useFetchData**           | Hook completo con `loading` + `data`.                                             | Reutilización + limpieza.                                      | Endpoint en `url`.                                         | `hooks/useFetchData.js`     |
| JavaScript  | React        | —                  | `snippets/react.json`           | Componente Listas  | **ListaDatos**             | Componente para pintar arrays personalizados.                                     | `renderItem` como prop.                                        | `renderItem` y nombre array.                               | `components/ListaDatos.jsx` |
| JavaScript  | React        | —                  | `snippets/react.json`           | Importación React  | **react-base**             | Importa `useState` y `useEffect`.                                                 | Inicio rápido.                                                 | —                                                          | `App.jsx`                   |
| JavaScript  | React        | —                  | `snippets/react.json`           | Componente base    | **componente-base**        | Crea componente funcional básico.                                                 | Boilerplate.                                                   | Nombre del componente.                                     | `App.jsx`                   |




# ⚡ Lista rápida de triggers (VS Code)
```bash
tpl-fa-app-sql       → Plantilla main.py con FastAPI + SQLModel + CRUD.
mod-pytest-fixtures  → conftest.py con BD en memoria + cliente de prueba.
mod-tests-crud       → Tests CRUD básicos (listar, crear, obtener, borrar).
mod-tests-extra      → Tests extra (422, 404, DELETE doble, done por defecto).
mod-reqs             → requirements.txt mínimo para FastAPI + Pytest.
mod-pytest-ini       → pytest.ini apuntando a carpeta tests.
mod-curl-post        → Comando curl para POST /tareas desde terminal.
fetch-loadTareas      → Función fetch para cargar tareas desde FastAPI.
fetch-condicional-done → Condicional JSX: ✅ Hecho / ⏳ Pendiente.
useEffect-load         → useEffect que ejecuta loadTareas al montar.
loading-state          → useState para gestionar cargando.
loader-condicional     → Mostrar <ul> o loader con ternario.
boton-refresh          → Botón genérico con Tailwind + onClick.
map-lista              → map para renderizar listas con <li>.
useFetchData           → Hook genérico reutilizable con loading y data.
ListaDatos             → Componente para renderizar listas con renderItem.
react-base             → Importación básica de useState y useEffect.
componente-base        → Componente base funcional de React.
```