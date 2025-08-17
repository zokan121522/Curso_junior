# 📂  test/conftest.py 🧪 Prepara un “laboratorio” limpio con una BD en memoria y un 
#            cliente falso para que todos los tests jueguen sin tocar la BD real.
 
# 1. Para que el test encuentre tu main.py aunque esté en la carpeta de arriba
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 2. Cargamos las herramientas:
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine
from sqlalchemy.pool import StaticPool
import main

# 3. Crea el motor de BD solo una vez para todos los tests. Vive en RAM, así no tocas tu archivo real.
@pytest.fixture(scope="session")
def test_engine():
    engine = create_engine(
        "sqlite://", # Base de datos temporal en RAM
        connect_args={"check_same_thread": False}, # Evita problemas con hilos
        poolclass=StaticPool, # Mantiene conexión viva
        echo=False, # No mostrar el SQL en consola
    )
    return engine

# 4. Antes de cada test, resetea la base de datos para que empiece vacía.
@pytest.fixture(autouse=True)
def _db_setup(test_engine):
    SQLModel.metadata.drop_all(test_engine) # Borra todas las tablas
    SQLModel.metadata.create_all(test_engine) # Las vuelve a crear limpias

# 5. Devuelve el cartero falso (client) que va a probar tu API sin arrancar servidor real.
@pytest.fixture()
def client(test_engine):
    main.engine = test_engine # Usa la BD de pruebas en vez de la real
    return TestClient(main.app) # Devuelve un cliente para hacer peticiones