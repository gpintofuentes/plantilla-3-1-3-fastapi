# Servicio de inferencia · plantilla 3.1.3 (FastAPI)

Repositorio base del servicio de inferencia del equipo. Trae la estructura completa,
`/health` funcionando y un **modelo demo de NovaSur** en `models/` para verificar el entorno.
El equipo reemplaza ese modelo por el de su caso cuando corresponda.

## Estructura

| Archivo | Paso | Estado en la plantilla | Sprint |
|---|---|---|---|
| `src/predictor.py` | 1 · Encapsular el modelo | Carga implementada; `predecir` por completar | 1 |
| `src/schemas.py` | 2 · Contrato de datos | Esquema de `/health`; entrada y salida por completar | 1 |
| `src/main.py` | 3 · La API | Ciclo de vida, CORS y `GET /health` listos | 1 |
| `tests/test_api.py` | 4 · Pruebas | Prueba de `/health` | 3 |
| `Dockerfile` | 5 · Contenedor | Esqueleto por completar | 2 |
| `requirements.txt` | — | Versiones fijadas | — |
| `models/` | — | Modelo demo de NovaSur y `metadata.json` | — |

## Ejecución local

Todo se ejecuta en **VS Code → Terminal → New Terminal**, con la carpeta del repositorio abierta (File → Open Folder).
Requiere Python 3.11 o superior.

| # | Para qué | Comando |
|---|---|---|
| 1 | Crear el entorno virtual (una vez) | `python -m venv .venv` |
| 2 | Instalar dependencias (una vez) | `.venv\Scripts\python -m pip install -r requirements.txt` |
| 3 | Levantar el servicio | `.venv\Scripts\python -m uvicorn src.main:app --reload` |
| 4 | Ejecutar las pruebas | `.venv\Scripts\python -m pytest -v` |

Verificación en el navegador: http://127.0.0.1:8000/health debe responder
`"modelo_cargado": true`. Documentación: http://127.0.0.1:8000/docs.
Para detener el servicio: `Ctrl + C` en la terminal.

## Reglas de trabajo en GitHub web

1. **Un responsable por archivo en cada sprint.** Solo esa persona sube ese archivo.
2. **Bajar antes de editar:** Code → Download ZIP (o el archivo puntual) antes de modificar en local.
3. **Subir con el número del issue:** Add file → Upload files, con un mensaje como `#4 endpoint batch`.

## Decisión de framework

| Requerimiento del caso | Criterio | Evidencia | Decisión |
|---|---|---|---|
| | | | |

**Framework seleccionado:** 
**Qué se cede con esta decisión:** 
**Qué cambiaría la decisión:** 

## Distribución de responsables

| Archivo | Sprint 1 | Sprint 2 | Sprint 3 |
|---|---|---|---|
| `src/predictor.py` | | | |
| `src/schemas.py` | | | |
| `src/main.py` | | | |
| `tests/test_api.py` | | | |
| `Dockerfile` | | | |

## Definición de terminado (DoD) del equipo

- [ ] Archivo subido al repositorio con el número del issue en el mensaje.
- [ ] Issue cerrado y tarjeta en «Terminado».
- [ ] `/health` sigue respondiendo y la ruta nueva aparece en la documentación.
- [ ] Desde el sprint 3: `pytest -v` aprobado.
