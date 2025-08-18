# 📍 Snippet: mod-auth-utils
# 🔐 Utilidad para validar tokens JWT y extraer usuario actual 📂 ├──auth_utils.py
from config import SECRET_KEY
from fastapi import Depends, HTTPException, Header
from jwt import decode, exceptions

# 🧠 Extrae y valida el token JWT desde la cabecera Authorization
def get_current_user(authorization: str = Header(...)):
    try:
        # 🔍 Separa el token del prefijo "Bearer"
        token = authorization.split(" ")[1]

        # 🔓 Decodifica el token con la clave secreta
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])

        # ✅ Devuelve el nombre de usuario si todo va bien
        return payload["sub"]

    # ⏰ Si el token está caducado, lanza error 401
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")

    # 🚫 Si cualquier otro error ocurre, lanza error 401
    except:
        raise HTTPException(status_code=401, detail="Token inválido")
    