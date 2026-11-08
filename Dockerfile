# Paso 5 · Sprint 2: completar este Dockerfile (ver Act 2.2).
# Requisitos:
#   - imagen base python:3.11-slim
#   - instalar requirements.txt sin caché de pip
#   - copiar src/ y models/
#   - ejecutar con un usuario sin privilegios (appuser)
#   - exponer el puerto 8000 y arrancar con: uvicorn src.main:app --host 0.0.0.0 --port 8000
FROM python:3.11-slim

# TODO sprint 2
