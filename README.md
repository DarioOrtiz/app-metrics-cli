# App Metrics CLI API

Servicio backend simple para gestionar información de aplicaciones.

Este proyecto expone una API construida con **FastAPI** y **GraphQL** que permite registrar y consultar aplicaciones.
Puede utilizarse como un pequeño servicio interno para **pipelines CI/CD, dashboards o herramientas de monitoreo**.

---

# Tecnologías

* Python 3.12
* FastAPI
* GraphQL (Strawberry)
* PostgreSQL
* Terraform (IaC para desplegar contenedores)
* Pydantic
* Uvicorn
* Requests (para pruebas)

---

# Arquitectura

El proyecto sigue una estructura simple basada en capas:

**API Layer (FastAPI)**
Expone endpoints REST y GraphQL.

**Service Layer**
Contiene la lógica de negocio.

**Data Layer**
Gestiona la persistencia de datos mediante PostgreSQL, garantizando almacenamiento confiable y consultas eficientes.

Esta estructura modular facilita extender el proyecto agregando nuevos servicios, validaciones o integraciones.

---

# Funcionalidades

* Registrar aplicaciones con nombre, versión y estado
* Consultar aplicaciones mediante API REST
* Consultar aplicaciones mediante GraphQL
* Base de datos: PostgreSQL, gestionada vía SQLAlchemy ORM
* Script simple de pruebas automatizadas
* Estructura modular fácil de extender

---

# Estructura del Proyecto

```
app-metrics-cli/
│
├── api/
│   ├── main.py        # Aplicación FastAPI
│   ├── db.py          # Inicialización de PostgreSQL
│   └── models.py      # Modelos de datos
│
├── services/          # Lógica de negocio
├── test_api.py        # Script de pruebas de la API
├── requirements.txt
└── README.md
```

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/DarioOrtiz/app-metrics-cli.git
cd app-metrics-cli
```

Crear entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install fastapi uvicorn strawberry-graphql requests
```
Instalar PostgreSQL (Ubuntu/Debian):
sudo apt update
sudo apt install postgresql postgresql-contrib

Crear base de datos y usuario:
sudo -u postgres psql
CREATE DATABASE app_metrics_db;
CREATE USER dario WITH ENCRYPTED PASSWORD 'metrics1234';
GRANT ALL PRIVILEGES ON DATABASE app_metrics_db TO dario;
\q

Inicializar base de datos:

```bash
python3 -c "from api import db; db.Base.metadata.create_all(bind=db.engine)"
```

Ejecutar la API:

```bash
uvicorn api.main:app --reload
```

---

# Quick Start

Una vez iniciada la API puedes acceder a:

**Swagger UI**

```
http://127.0.0.1:8000/docs
```

Desde allí puedes:

* Crear aplicaciones
* Consultar aplicaciones registradas
* Probar los endpoints REST

También puedes probar GraphQL en:

```
http://127.0.0.1:8000/graphql
```

---

# Endpoints de la API

## REST

### Agregar aplicación

POST `/apps/`

Ejemplo de request:

```json
{
  "name": "MiApp",
  "version": "1.0",
  "status": "active"
}
```

### Listar aplicaciones

GET `/apps/`

Ejemplo de respuesta:

```json
[
  {
    "id": 1,
    "name": "MiApp",
    "version": "1.0",
    "status": "active"
  }
]
```

---

# Ejemplo usando curl

Crear una aplicación desde terminal:

```bash
curl -X POST http://127.0.0.1:8000/apps/ \
-H "Content-Type: application/json" \
-d '{
"name": "TestApp",
"version": "1.0",
"status": "active"
}'
```

---

# GraphQL

Endpoint:

```
POST /graphql
```

Ejemplo de consulta:

```graphql
query {
  apps {
    id
    name
    version
    status
  }
}
```

Playground disponible en:

```
http://127.0.0.1:8000/graphql
```

---

## Pruebas Automatizadas

El proyecto incluye varias formas de validar el funcionamiento de la API y comprobar que los endpoints funcionan correctamente.

### 1. Script de pruebas general

Archivo:

test_api.py

Este script realiza pruebas básicas sobre la API, incluyendo:

- Creación de aplicaciones
- Consulta de aplicaciones vía REST
- Consulta de aplicaciones vía GraphQL

Para ejecutarlo:

python test_api.py

### 2. Prueba de integración

Archivo:

tests/test_app.py

Este script utiliza la librería requests para interactuar con la API en ejecución y realiza:

- Creación de aplicaciones
- Consulta de aplicaciones vía REST

Para ejecutarlo, primero asegúrate de que la API esté corriendo y luego ejecuta:

python tests/test_app.py

### 3. Pruebas con FastAPI TestClient

Archivo:

tests/test_main.py

Estas pruebas utilizan TestClient de FastAPI para validar los endpoints directamente dentro de la aplicación. Se verifican aspectos como:

- Creación de aplicaciones
- Consulta de aplicaciones
- Respuestas correctas de la API

Para ejecutarlas:

pytest

Estas pruebas permiten validar rápidamente que la API funciona correctamente y facilitan futuras ampliaciones del proyecto.

---

# Posibles mejoras futuras

* Autenticación y autorización mediante JWT.
* Dockerización del servicio para facilitar despliegue y entornos consistentes.
* Métricas y monitoreo con Prometheus.
* Integración en pipelines CI/CD para despliegue automático y pruebas.
