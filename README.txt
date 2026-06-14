# PeopleFlow Employees API

API REST desarrollada con FastAPI y MongoDB para la gestión de empleados.

## Features

* Employee CRUD
* Employee salary average calculation
* JWT Authentication
* Swagger/OpenAPI documentation
* MongoDB persistence
* Docker support

---

## Tecnologías utilizadas

* Python 3.13
* FastAPI
* MongoDB
* PyMongo
* JWT Authentication
* Docker
* Swagger / OpenAPI
* Pytest

---

## Arquitectura

El proyecto sigue una arquitectura por capas:

```text
Controller -> Service -> Repository -> MongoDB
```

### Estructura del proyecto

```text
app/
├── api/
│   ├── auth_controller.py
│   └── employee_controller.py
│
├── core/
│   ├── config.py
│   └── security.py
│
├── database/
│   └── mongo.py
│
├── repositories/
│   └── employee_repository.py
│
├── schemas/
│   ├── auth_schema.py
│   └── employee_schema.py
│
├── services/
│   └── employee_service.py
│
└── main.py
```

---

## Funcionalidades

### Gestión de empleados

* Crear empleado
* Obtener todos los empleados
* Obtener empleado por ID
* Actualizar empleado
* Eliminar empleado
* Obtener salario promedio

### Seguridad

* Autenticación mediante JWT
* Protección de endpoints mediante Bearer Token

### Extras

* Swagger/OpenAPI
* Docker
* Validaciones con Pydantic
* Variables de entorno mediante `.env`

---

## Variables de entorno

### Desarrollo local

Crear un archivo `.env` en la raíz del proyecto:

```env
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=peopleflow

JWT_SECRET_KEY=peopleflow_secret_2026
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
```

### Docker

El proyecto incluye un archivo `.env.docker` para la ejecución mediante Docker Compose.

```env
MONGO_URI=mongodb://mongo:27017
DATABASE_NAME=peopleflow

JWT_SECRET_KEY=peopleflow_secret_2026
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
```

---

## Instalación local

### Clonar repositorio

```bash
git clone https://github.com/FedeVazquez/ChallengeLeafnoise.git
cd ChallengeLeafnoise
```

### Crear entorno virtual

```bash
python -m venv .venv
```

### Activar entorno virtual

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar aplicación

```bash
uvicorn app.main:app --reload
```

---

## Ejecución con Docker

### Construir y levantar servicios

```bash
docker compose up --build
```

### Ejecutar en segundo plano

```bash
docker compose up -d --build
```

### Detener servicios

```bash
docker compose down
```

---

## Documentación

Swagger UI:

```text
http://localhost:8000/docs
```

OpenAPI JSON:

```text
http://localhost:8000/openapi.json
```

---

## Autenticación

### Login

```http
POST /auth/login
```

Body:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Respuesta:

```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

### Uso del token

1. Ejecutar el endpoint `/auth/login`.
2. Copiar el token JWT generado.
3. Presionar el botón **Authorize** en Swagger.
4. Pegar el token.
5. Consumir los endpoints protegidos.

---

## Endpoints

### Auth

| Método | Endpoint    |
| ------ | ----------- |
| POST   | /auth/login |

### Employees

| Método | Endpoint                        |
| ------ | ------------------------------- |
| POST   | /employees                      |
| GET    | /employees                      |
| GET    | /employees/{employee_id}        |
| PUT    | /employees/{employee_id}        |
| DELETE | /employees/{employee_id}        |
| GET    | /employees/stats/salary-average |

---

## Ejemplo de creación de empleado

Request:

```json
{
  "nombre": "Federico",
  "apellido": "Vazquez",
  "email": "federico@gmail.com",
  "puesto": "Backend Developer",
  "salario": 10000,
  "fecha_ingreso": "2026-06-14"
}
```

Response:

```json
{
  "id": "6a2ed3f3b2f0af2851aac808",
  "nombre": "Federico",
  "apellido": "Vazquez",
  "email": "federico@gmail.com",
  "puesto": "Backend Developer",
  "salario": 10000,
  "fecha_ingreso": "2026-06-14"
}
```

---

## Ejemplo de salario promedio

Request:

```http
GET /employees/stats/salary-average
```

Response:

```json
{
  "average_salary": 10000
}
```

---

## Autor

Federico Vazquez Barbera

Backend Developer
