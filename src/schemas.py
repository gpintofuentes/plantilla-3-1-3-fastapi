"""
Paso 2 · Contrato de datos.

Plantilla 3.1.3: solo trae el esquema de /health. Los esquemas de entrada y
salida se completan en el sprint 1, con el diccionario de datos del caso.
"""
from pydantic import BaseModel, Field  # noqa: F401  (Field se usa al completar los esquemas)


class Salud(BaseModel):
    estado: str
    modelo_cargado: bool
    version_modelo: str


# TODO sprint 1: esquema de entrada con tipos, rangos y formatos del caso.
# Ejemplo de la forma (no del caso de tu equipo):
#
# class Registro(BaseModel):
#     cliente_id: str = Field(pattern=r"^CLI-[0-9]{6,10}$")
#     antiguedad_meses: int = Field(ge=1)
#
# TODO sprint 1: esquema de salida (predicción y versión del modelo).
