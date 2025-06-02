# Guía de Trabajo con Docker – Proyecto NimbusCore

Esta guía documenta el flujo de trabajo con Docker para el equipo de desarrollo del proyecto **NimbusCore**, eliminando la necesidad de entornos locales individuales.

---

## 🐳 1. Levantar Servicios

Desde la raíz del proyecto:

```bash
docker compose up -d --build
```

Esto:

* Construye las imágenes (si hay cambios).
* Levanta los contenedores de Django, PostgreSQL y SonarQube.

---

## 📜 2. Ver Logs

Para ver logs en tiempo real:

```bash
docker compose logs -f web
```

O por contenedor:

```bash
docker logs web
# o
docker logs postgres_nimbuscore
```

---

## 🧪 3. Ejecutar Comandos desde Docker

```bash
docker exec -it django_nimbuscore bash
```

Ejemplos desde dentro del contenedor:

```bash
python manage.py runserver
```

---

## ⚙️ 4. Flujo de Desarrollo

* Puedes editar el código con VSCode como siempre.
* Los cambios se reflejan automáticamente en Flask si está en modo `debug=True`.
* No necesitas instalar nada en tu máquina salvo Docker y Docker Compose.

---

## 🔎 5. Análisis con SonarQube

Ejecutar análisis manual:

```bash
docker run --rm \
  -e SONAR_HOST_URL="http://172.17.0.1:9000" \
  -e SONAR_TOKEN="sqp_bfb298a7f59ed6934e7819e85dc22f5e9150f4cd" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

---
