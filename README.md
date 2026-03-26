App Metrics CLI API

Servicio backend simple para gestionar información de aplicaciones.

Este proyecto expone una API construida con FastAPI y GraphQL que permite registrar y consultar aplicaciones.
Puede utilizarse como un pequeño servicio interno para pipelines CI/CD, dashboards o herramientas de monitoreo.

Tecnologías
Python 3.12
FastAPI
GraphQL (Strawberry)
SQLite
Pydantic
Uvicorn
Requests (para pruebas)
Funcionalidades
Registrar aplicaciones con nombre, versión y estado
Consultar aplicaciones mediante API REST
Consultar aplicaciones mediante GraphQL
Base de datos ligera con SQLite
Script simple de pruebas automatizadas
Estructura modular fácil de extender
Estructura del Proyecto
app-metrics-cli/
│
├── api/
│   ├── main.py        # Aplicación FastAPI
│   ├── db.py          # Inicialización de SQLite
│   └── models.py      # Modelos de datos
│
├── services/          # Lógica de negocio
├── test_api.py        # Script de pruebas de la API
├── requirements.txt
└── README.md
Instalación

Clonar el repositorio:

git clone https://github.com/DarioOrtiz/app-metrics-cli.git
cd app-metrics-cli

Crear entorno virtual:

python3 -m venv venv
source venv/bin/activate

Instalar dependencias:

pip install fastapi uvicorn strawberry-graphql requests

Inicializar base de datos:

python3 -c "from api import db"

Ejecutar la API:

uvicorn api.main:app --reload
Endpoints de la API
REST

Agregar aplicación

POST /apps/

Ejemplo de request:

{
  "name": "MiApp",
  "version": "1.0",
  "status": "active"
}

Listar aplicaciones

GET /apps/

Ejemplo de respuesta:

[
  {
    "id": 1,
    "name": "MiApp",
    "version": "1.0",
    "status": "active"
  }
]
GraphQL

Endpoint:

POST /graphql

Ejemplo de consulta:

query {
  apps {
    id
    name
    version
    status
  }
}

Playground disponible en:

http://127.0.0.1:8000/graphql
Pruebas Automatizadas

El proyecto incluye un script de pruebas:

test_api.py

Este script realiza:

Creación de aplicaciones
Consulta de aplicaciones vía REST
Consulta de aplicaciones vía GraphQL

Proyecto modular y extensible:

Agregar nuevos endpoints REST/GraphQL
Integrar con bases de datos externas
Añadir autenticación y autorización
Integrar pruebas automáticas en pipelines DevOps