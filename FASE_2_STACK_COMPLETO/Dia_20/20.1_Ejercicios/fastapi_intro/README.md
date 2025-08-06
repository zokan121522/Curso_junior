# 🧠 Proyecto FastAPI – Día 20

Este proyecto es una API básica con FastAPI que incluye dos endpoints:

- `GET /saludo`: Devuelve un mensaje de bienvenida.
- `POST /perfil`: Recibe un perfil en formato JSON y lo devuelve procesado.

## 🚀 Cómo ejecutar el proyecto

```bash
# Clona el repositorio y entra a la carpeta
git clone https://github.com/tuusuario/fastapi-dia20
cd fastapi-dia20

# Crea entorno virtual y actívalo
python3 -m venv env
source env/bin/activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el servidor
uvicorn main:app --reload
```
