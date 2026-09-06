import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "UP"}
    
def test_version():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200
    assert "version" in response.json


def test_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")

    client = app.test_client()

    response = client.get("/environment")

    assert response.status_code == 200
    assert response.json["environment"] == "development"
    
def test_services():
    client = app.test_client()

    response = client.get("/services")

    assert response.status_code == 200
    assert "services" in response.json
    assert len(response.json["services"]) > 0