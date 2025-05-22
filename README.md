# NimbusCore

Plataforma web segura para administrar servicios de un conjunto de servidores Linux.  
El sistema permite registrar servidores, levantar servicios, administrarlos y monitorizarlos en tiempo real.  
Todo el desarrollo se realiza con **Django + PostgreSQL**, y se despliega en contenedores Docker.

## 🧱 Estructura general

```
NimbusCore/
├── backend/                  # Proyecto Django
│ ├── core/                   # Proyecto base de Django
│ ├── app/                    # App principal (login, vistas, templates)
│ ├── static/                 # Archivos estáticos
│ └── templates/              # Plantillas HTML
├── .env                      # Variables de entorno
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
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
sudo docker-compose up -d --build
```

Esto iniciará los siguientes contenedores:

* `django_nimbuscore`: backend con django
* `postgres_nimbuscore`: base de datos PostgreSQL
* `sonarqube`: servidor de calidad de código (opcional)

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

* [x] Docker Compose para backend, DB y SonarQube
* [x] Login simple
* [x] Integración con PostgreSQL
* [ ] Protección con JWT
* [ ] Verificación de usuarios reales con base de datos
* [ ] Módulo de registro de servidores y servicios

---

> Proyecto realizado para la E.E. Programación Segura - 2025
