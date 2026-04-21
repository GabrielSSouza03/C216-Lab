from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_query_param():
    response = client.get("/api/v1/hello?name=Matheus")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Matheus"}


def test_path_param():
    response = client.get("/api/v1/hello/Matheus")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Matheus"}


def test_post():
    response = client.post(
        "/api/v1/hello",
        json={"name": "Matheus"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Matheus"}

def test_post_invalid():
    response = client.post("/api/v1/hello", json={})
    assert response.status_code == 422


def test_put():
    response = client.put(
        "/api/v1/update",
        json={"name": "Matheus"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Recurso atualizado com o nome: Matheus"}


def test_delete():
    response = client.delete("/api/v1/delete?name=Matheus")
    assert response.status_code == 200
    assert response.json() == {"message": "Recurso deletado com o nome: Matheus"}


def test_patch():
    response = client.patch(
        "/api/v1/patch",
        json={"name": "Matheus"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Modificação parcial aplicada ao recurso com o nome: Matheus"}


def test_api_status():
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "api": "v1"}


def test_calc_sum():
    response = client.get("/api/v1/calc/sum?a=10&b=32")
    assert response.status_code == 200
    assert response.json() == {"result": 42}


def test_calc_sum_negative():
    response = client.get("/api/v1/calc/sum?a=-5&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 0}


def test_code_ok():
    response = client.get("/api/v1/codes/ok")
    assert response.status_code == 200
    assert response.json() == {"code": "ok", "valid": True}


def test_code_200_alias():
    response = client.get("/api/v1/codes/200")
    assert response.status_code == 200
    assert response.json() == {"code": "200", "valid": True}


def test_code_not_found():
    response = client.get("/api/v1/codes/unknown")
    assert response.status_code == 404
    assert response.json()["detail"] == "Código não encontrado"


def test_ping_head():
    response = client.head("/api/v1/ping")
    assert response.status_code == 204
    assert response.content == b""


def test_post_items():
    response = client.post(
        "/api/v1/items",
        json={"name": "Caderno", "qty": 3},
    )
    assert response.status_code == 200
    assert response.json() == {
        "received": "Caderno",
        "qty": 3,
        "note": "Registrado: 3 unidade(s) de Caderno",
    }


def test_post_items_invalid():
    response = client.post("/api/v1/items", json={"name": "X"})
    assert response.status_code == 422