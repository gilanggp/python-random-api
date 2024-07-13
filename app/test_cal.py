from fastapi.testclient import TestClient
from .cal import app

client = TestClient(app)


def test_cal_func():
    response = client.get("/cal/12+3")
    assert response.status_code == 200
    assert response.json() == {"command": "12+3", "result": 15.0}