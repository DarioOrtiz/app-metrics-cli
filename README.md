# app-metrics-cli

Proyecto de ejemplo para mostrar habilidades backend + DevOps:

- API en Python (FastAPI + SQLite)
- CLI en Golang
- Docker y Terraform para infraestructura
- CI/CD (opcional)

## Ejecutar API localmente

```bash
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload# app-metrics-cli
