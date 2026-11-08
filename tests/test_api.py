"""
Paso 4 · Pruebas (se completan en el sprint 3).
Ejecutar desde la raíz del repositorio:  .venv\\Scripts\\python -m pytest -v
"""
from fastapi.testclient import TestClient

from src.main import app


def test_health_responde_200_con_modelo_cargado():
    with TestClient(app) as cliente:  # el "with" ejecuta el ciclo de vida (carga el modelo)
        r = cliente.get("/health")
    assert r.status_code == 200
    assert r.json()["modelo_cargado"] is True


# TODO sprint 3: pruebas de /v1/predict, /v1/predict/batch y de datos inválidos (422 o 400)
