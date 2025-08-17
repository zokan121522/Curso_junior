# ⚡Comandos útiles (Entorno y Conexión)

| 📌 Concepto               | 📖 Explicación **técnica**                                 | 💻 Comando real / Código                | 💬 Explicación coloquial                                | 🟢 🟠 🔴 |
| ------------------------- | ---------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------- | -------- |
| 🌍 **Entorno virtual**    | Carpeta aislada con dependencias específicas del proyecto. | `python3 -m venv env`                   | 🏠 “Tu caja de arena privada.”                          | 🟢       |
| 🟢 **Activar entorno**    | Usar las librerías del entorno virtual.                    | `source env/bin/activate`               | 🔌 “Conectas la corriente para trabajar aquí dentro.”   | 🟢       |
| 🔴 **Desactivar entorno** | Salir del entorno virtual.                                 | `deactivate`                            | 🚪 “Cierras la caja de arena y vuelves al mundo real.”  | 🟢       |
| 📂 **Instalar paquetes**  | Instala todas las dependencias desde un archivo.           | `pip install -r requirements.txt`       | 🛒 “Vas con la lista de la compra y llenas el carrito.” | 🟢       |
| 📝 **Archivo .env**       | Variables ocultas de entorno (claves, DB, puertos).        | `DATABASE_URL="sqlite:///test.db"`      | 🔑 “La libreta secreta de contraseñas/configuración.”   | 🟠       |
| ⚙ **Levantar servidor**   | Arranca el backend con autoreload.                         | `uvicorn main:app --reload`             | ⚡ “El motor que pone en marcha la API.”                 | 🟠       |
| 🚪 **Liberar puerto**     | Ver qué proceso ocupa el puerto.                           | `lsof -nP -iTCP:8000 \| grep LISTEN`    | 🔍 “Miras quién está usando la puerta 8000.”            | 🔴       |
| 🔨 **Matar proceso**      | Forzar cierre de un proceso por su PID.                    | `kill -9 67635`                         | 💣 “Cierras a la fuerza al que ocupa tu puerto.”        | 🔴       |
| 🛡 **Matar uvicorn**      | Cierra cualquier uvicorn que siga vivo.                    | `pkill -9 -f uvicorn`                   | 🚷 “Barres todos los servidores fantasma.”              | 🔴       |
| 🔌 **Cambiar puerto**     | Levantar API en otro puerto.                               | `uvicorn main:app --reload --port 8001` | 📡 “Usas otra puerta porque la primera está ocupada.”   | 🟠       |
|                           |                                                            |                                         |                                                         |          |

