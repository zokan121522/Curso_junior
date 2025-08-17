# 📦 1. Importamos FastAPI y SQLModel
from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select

# 🚀 2. Creamos instancia FastAPI
app = FastAPI()

# 🧑‍💻 3. Definimos modelo de tabla: Usuario
class Usuario(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    edad: int

# 🛠️ 4. Creamos motor de base de datos SQLite (archivo local)
sqlite_url = "sqlite:///./usuarios.db"
engine = create_engine(sqlite_url, echo=True)

# 🏗️ 5. Creamos las tablas si no existen
def crear_tablas():
    SQLModel.metadata.create_all(engine)

crear_tablas()  # Se ejecuta una vez al iniciar

# 📬 Ruta para guardar usuario (POST)
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    with Session(engine) as session:
        session.add(usuario)       # Añadimos usuario a sesión
        session.commit()           # Guardamos en la base de datos
        session.refresh(usuario)   # Refrescamos para obtener el ID
        return usuario             # Se devuelve el usuario creado (con ID)

# 📥 Ruta para obtener todos los usuarios
@app.get("/usuarios")
def obtener_usuarios():
    with Session(engine) as session:
        resultado = session.exec(select(Usuario))  # Consulta SELECT *
        usuarios = resultado.all()
        return usuarios