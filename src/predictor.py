"""
Paso 1 · Encapsular el modelo.

Plantilla 3.1.3: la carga del modelo ya está implementada para que /health
responda. La predicción se completa en el sprint 1.
"""
import json
from pathlib import Path

import joblib


class Predictor:
    """Envuelve el archivo .joblib y las reglas de negocio del caso."""

    def __init__(self, ruta_modelo: Path):
        self.ruta_modelo = Path(ruta_modelo)
        self.modelo = None
        self.metadata: dict = {}
        if self.ruta_modelo.exists():
            self.modelo = joblib.load(self.ruta_modelo)  # una sola vez, al iniciar
            ruta_meta = self.ruta_modelo.with_name("metadata.json")
            if ruta_meta.exists():
                self.metadata = json.loads(ruta_meta.read_text(encoding="utf-8"))

    @property
    def cargado(self) -> bool:
        return self.modelo is not None

    @property
    def version(self) -> str:
        return self.metadata.get("version_modelo", "sin-version")

    def predecir(self, registros: list[dict]) -> list[dict]:
        """Recibe una lista de registros (uno o varios) y devuelve una lista de predicciones.

        TODO sprint 1:
          1. Armar la matriz de entrada con las columnas en el MISMO orden del
             entrenamiento (ver "atributos" en models/metadata.json).
          2. Llamar a self.modelo.predict_proba(...).
          3. Aplicar la regla de negocio del caso (umbrales, nivel de riesgo, etc.).
        """
        raise NotImplementedError("Completar en el sprint 1")
