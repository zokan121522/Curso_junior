from fastapi import FastAPI , HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()



usuarios = {
    1 : {"nombre" : "Jaime", "edad" : 41},
    2 : {"nombre" : "Jesica", "edad" : 40},
    3 : {"nombre" : "Zokan", "edad" : 18}
}

@app.get("/usuarios/{id}")

def buscarUsuarios(id : int):
    if id not in usuarios:
        raise HTTPException(
            status_code=400,
            detail=f"Usuario con id {id} no encontrado"
        )
    return JSONResponse(
        content={
            "usuario": usuarios[id],
            "mensaje": f"Hola, {usuarios[id]['nombre']} con {usuarios[id]['edad']} años"
        },
        status_code= 200
    )
