# test/test_api.py
# Lee un test {Patrón: petición → assert status_code → assert datos}

# 📝 test_listar_vacio → 📥 GET lista → ✅ 200 + 📄 []
def test_listar_vacio(client):
    resp = client.get("/tareas")
    assert resp.status_code == 200
    assert resp.json() == []

# ➕ test_crear_tarea_ok → 📤 POST nueva tarea → ✅ 201 + 🆔✔ + 📄 datos correctos
def test_crear_tarea_ok(client):
    nueva = {"titulo": "Escribir tests", "done": False}
    resp = client.post("/tareas", json=nueva)
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] is not None
    assert data["titulo"] == "Escribir tests"
    assert data["done"] is False

# 🔍 test_get_por_id_ok → 📤 POST crea → 📥 GET por id → ✅ 200
def test_get_por_id_ok(client):
    r = client.post("/tareas", json={"titulo": "Buscar por id", "done": False})
    tid = r.json()["id"]
    resp = client.get(f"/tareas/{tid}")
    assert resp.status_code == 200

# ❌ test_borrar_tarea_ok → 📤 POST crea → 🗑 DELETE → ✅ 204 + 🚫 que no esté en lista
def test_borrar_tarea_ok(client):
    r = client.post("/tareas", json={"titulo": "Borrar luego", "done": False})
    tid = r.json()["id"]
    del_r = client.delete(f"/tareas/{tid}")
    assert del_r.status_code == 204
    lista = client.get("/tareas").json()
    assert all(t["id"] != tid for t in lista)