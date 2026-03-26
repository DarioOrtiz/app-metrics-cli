App Metrics CLI API

API para gestión de aplicaciones, desarrollada en Python con FastAPI y GraphQL.
Permite agregar, listar y consultar aplicaciones mediante REST y GraphQL, ideal para integraciones en pipelines CI/CD, dashboards internos o herramientas de monitoreo de aplicaciones.

Tecnologías usadas
Python 3.12
FastAPI – Framework web moderno para APIs REST
SQLite – Base de datos ligera embebida
Strawberry – Integración de GraphQL con Python
Pydantic – Validación y serialización de datos
Requests – Cliente HTTP para pruebas
Uvicorn – Servidor ASGI para FastAPI

Opcional para DevOps y despliegues:

Docker
GitHub Actions / GitLab CI para integración continua
Funcionalidades
Agregar aplicaciones con name, version y status.
Listar aplicaciones desde REST (/apps/) o GraphQL (/graphql).
Consultas GraphQL para obtener información estructurada de las apps.
Arquitectura modular, lista para ampliar con más endpoints, servicios o integraciones.
Pruebas automatizadas con scripts Python (test_api.py) para validar la API.
Instalación y ejecución
Clonar el repositorio:
# Con SSH
git clone git@github.com:DarioOrtiz/app-metrics-cli.git
# Con HTTPS
git clone https://github.com/DarioOrtiz/app-metrics-cli.git
cd app-metrics-cli
Crear un entorno virtual:
python3 -m venv venv
source venv/bin/activate
Instalar dependencias:
pip install fastapi uvicorn strawberry-graphql requests
Inicializar la base de datos (SQLite):
python3 -c "from api import db"
Ejecutar la API localmente:
uvicorn api.main:app --reload
REST disponible en: http://127.0.0.1:8000/apps/
GraphQL playground en: http://127.0.0.1:8000/graphql
Endpoints
REST

POST /apps/ – Agregar una app

{
  "name": "MiApp",
  "version": "1.0",
  "status": "active"
}

GET /apps/ – Listar todas las apps

[
  {
    "id": 1,
    "name": "MiApp",
    "version": "1.0",
    "status": "active"
  }
]
GraphQL
POST /graphql – Consultas GraphQL
{
  apps {
    id
    name
    version
    status
  }
}
Pruebas automatizadas

Se incluye un script de prueba test_api.py que:

Agrega varias apps
Lista apps usando REST
Consulta apps usando GraphQL

Ejecutar:

python3 test_api.py
Integración en pipelines CI/CD
Docker: Puedes dockerizar la API para pruebas o despliegues automáticos.
GitHub Actions / GitLab CI: Automatiza pruebas del script test_api.py en cada commit.
Monitoreo: Con REST y GraphQL puedes integrar métricas de apps a dashboards internos o sistemas de alertas.
Contribuciones

Proyecto modular y extensible:

Agregar nuevos endpoints REST/GraphQL
Integrar con bases de datos externas
Añadir autenticación y autorización
Integrar pruebas automáticas en pipelines DevOps