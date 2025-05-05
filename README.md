# NimbusCore

App web para registrar servidores Linux y gestionar los servicios instalados en ellos: levantarlos, administrarlos (reiniciar/dar de baja) y monitorizarlos en tiempo real.

## Tecnologías

* **Frontend**: Aplicación Flutter (Web y Móvil)
* **Backend**: API REST con Flask, PostgreSQL, JWT, Swagger (Flasgger)
* **Contenedores**: Docker + Docker Compose

## Estructura del proyecto

```
NimbusCore/
├── backend/
│   ├── app/
│   │   ├── api/                # Futura API para Flutter
│   │   ├── core/               # Inicialización de extensiones
│   │   ├── docs/               # Documentación Swagger
│   │   ├── forms/              # Formularios WTForms para vista de prueba
│   │   ├── models/             # Modelos SQLAlchemy
│   │   ├── routes/             # Rutas Flask
│   │   ├── templates/          # HTML para prueba con login
│   │   ├── config.py           # Configuración general
│   │   └── __init__.py         # Fábrica de la app
│   ├── run.py                  # Entry point
│   ├── requirements.txt        # Dependencias
│   ├── Dockerfile              # Imagen del backend
│   └── .env                    # Variables de entorno
├── frontend/                   # Aplicación Flutter
├── docker-compose.yml          # Orquestación de servicios
```

## Instalación y ejecución

### 📁 1. Clonar el repositorio

```bash
git clone https://github.com/jesusgvqz/NimbusCore.git
cd NimbusCore
```

---

### 🚧 2. Levantar los servicios con Docker Compose

```bash
docker compose up -d --build
```

Esto iniciará los siguientes contenedores:

* `flask_backend`: backend con Flask
* `postgres_nimbuscore`: base de datos PostgreSQL
* `sonarqube`: servidor de calidad de código (opcional)

### 🔧 3. Acceder a la app de prueba

* API REST: [http://localhost:5000](http://localhost:5000)
* Swagger UI: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)
* Login de prueba: [http://localhost:5000/login](http://localhost:5000/login)

  * Usuario: `admin` / Contraseña: `admin`

---

### 🌐 4. Frontend Flutter (opcional por ahora)

La estructura ya está preparada para conectar Flutter a la API.

#### A. Ir a la carpeta del frontend

```bash
cd frontend
```

#### B. Verifica que tienes Flutter instalado

```bash
flutter doctor
```

#### C. Ejecutar la app Flutter

```bash
flutter run -d chrome    # En web
flutter run              # En emulador o dispositivo
```

---

## 🔒 Variables de entorno

Ejemplo de `.env` para el backend:

```
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=superjwtsecret
JWT_ACCESS_TOKEN_EXPIRES=3600
JWT_TOKEN_LOCATION=headers
DATABASE_URL=postgresql://user:pass:5432/database
```

Puedes copiar desde el archivo `.env.example` si está disponible:

```bash
cp .env.example .env
```

---

## 🚫 Notas

* El login HTML es temporal. Todo se migrará a API REST para consumo desde Flutter.
* El backend implementa CSRF y JWT.

---

## 📊 En desarrollo

* [x] Login simple con WTForms
* [x] Integración con PostgreSQL
* [x] Documentación Swagger
* [x] Protección con JWT
* [x] Docker Compose para backend, DB y SonarQube
* [ ] API REST completa para Flutter
* [ ] Verificación de usuarios reales con base de datos
* [ ] Autenticación con roles
* [ ] Módulo de registro de servidores y servicios

---

> Proyecto realizado para la E.E. Programación Segura - 2025
