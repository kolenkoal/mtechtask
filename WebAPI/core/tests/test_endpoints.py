from fastapi.testclient import TestClient
# from ..endpoints.endpoints import router
from ..endpoints.endpoints import router

client = TestClient(router)


def test_process_log_valid():
    valid_log_data = {
        "log": "192.168.1.1 GET /example 200"
    }

    response = client.post("/api/data/", json=valid_log_data)
    assert response.status_code == 201
    assert response.json() == {"message": "Лог сохранен"}


def test_process_log_invalid():
    invalid_log_data = {
        "log": "Invalid log data"
    }

    response = client.post("/api/data/", json=invalid_log_data)
    assert response.status_code == 418
    assert response.json() == {"detail": "Что-то пошло не так"}
