# 1. Importamos FastAPI y SQLModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel,Field,create_engine,Session,select
# 2. Instancia de la APP
app = FastAPI()

# 3. Modelo de tabla: tareas
class Tarea(SQLModel,table=True):
    id : int = Field(default=None,primary_key=True) 
    titulo : str
    done : bool = False
# Nota    
#       1. Hacemos un (clave:valor) pq se un .json 
#       2. El {id} lo pasamos Numero 
#       3. Abrimos la carpeta con dos atributos(por defecto,clave primera) 
#       4. titulo es un string 
#       5. Hecha : o no (por defecto False)   

# 4. Motor SQLite (archivo local)
engine = create_engine("sqlite:///./tarea.db", echo=True)
# Nota 
#       1. Instancia engine es igual  = 
#       2. Creamos engine con dos atributos(dirección, que se vean todos los parametros)

# 5. Creamos la tabla con (def)
def crear_tabla():
    SQLModel.metadata.create_all(engine)
crear_tabla()
# Nota 
#       1. Nombre de la funcion (): 
#       2. Mira estos planos y construye la tabla en la base de datos usando la conexión (engine)


# 6. POST / tareas - Crear tareas
@app.post("/tareas",status_code=201)
def crear_tarea(tarea:Tarea):
    with Session (engine) as session:
        session.add(tarea)
        session.commit()
        session.refresh(tarea)
        return tarea
# Nota 
#       1. Creamos el decorador POST para crear con dos atributos (ruta y estado) 
#       2. Creamos la funcion con (clave:valor) JSON
#       3. Con Session : abrimos,metemos,sacamos o borramos cosas en (engine) con session: 
#           3.1 Añade una tarea 
#           3.2 Guarda una tarea 
#           3.3 Obtiene {id} autogenerado 
#           3.4 Devuelve la tarea creada con id exclusivo

# 7. GET / tareas - listar tareas
app.get("/tareas")
def listar_tareas():
    with Session(engine) as session:
        result = session.exec(select(Tarea))
        return result.all()

# Nota 
#       1. Creamos el decorador GET para leer con una ruta de acceso (/tareas)
#       2. Creamos y nombramos la función para listar
#       3. Abrimos conexión temporal con la base de datos
#       4. Pedimos todas las tareas guardadas
#       5. Devolvemos la lista completa



# 8. DELETE / tareas - eliminar tareas con {id} exclusivo 

@app.delete("/tareas/{id}",status_code=204)
def borrar_tarea():
    


# Nota 
#       1. Creamos el decorador de borrar la tarea 
#           con dos atributos (direccion, mensaje del borrado) 
#       2. Creamos la funcion para borrar la tarea 