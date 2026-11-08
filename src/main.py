"""
Paso 3 · La API (variante FastAPI).

Plantilla 3.1.3: ciclo de vida, CORS y /health funcionando.
Las rutas de predicción se completan en el sprint 1.
"""
import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.predictor import Predictor
from src.schemas import Salud

RAIZ = Path(__file__).resolve().parents[1]
RUTA_MODELO = Path(os.getenv("RUTA_MODELO", RAIZ / "models" / "modelo_churn_novasur.joblib"))

recursos: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    recursos["predictor"] = Predictor(RUTA_MODELO)  # se carga una sola vez
    yield
    recursos.clear()


app = FastAPI(title="Servicio de inferencia", version="0.1.0", lifespan=lifespan)

# CORS: permite que un consumidor web llame al servicio. Restringir los orígenes en producción.
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/health", response_model=Salud)
def health():
    p = recursos.get("predictor")
    return Salud(
        estado="ok",
        modelo_cargado=bool(p and p.cargado),
        version_modelo=p.version if p else "sin-version",
    )


# TODO sprint 1: POST /v1/predict        -> un registro
# TODO sprint 1: POST /v1/predict/batch  -> lista acotada de registros
