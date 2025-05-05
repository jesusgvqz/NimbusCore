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
* Levanta los contenedores de Flask, PostgreSQL y SonarQube.

---

## 📜 2. Ver Logs

Para ver logs en tiempo real:

```bash
docker compose logs -f flask_backend
```

O por contenedor:

```bash
docker logs flask_backend
# o
docker logs postgres_nimbuscore
```

---

## 🧪 3. Ejecutar Comandos en Flask (desde Docker)

```bash
docker exec -it flask_backend bash
```

Ejemplos desde dentro del contenedor:

```bash
python run.py
flask shell
flask db upgrade
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
  -e SONAR_TOKEN="sqp_da6bbed3337ac0b5d611a6ba5a1c150005212790" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

---

## 🧹 Archivos Eliminables

| Archivo/Directorio   | ¿Borrar?   | Justificación                        |
| -------------------- | ---------- | ------------------------------------ |
| `venv/`              | ✅ Sí       | Docker reemplaza el entorno local    |
| `.flaskenv`          | ✅ Sí       | Variables ahora están en `.env`      |
| `makefile`           | ✅ Opcional | Docker cubre todo el flujo           |
| `.env`               | ❌ No       | Necesario para credenciales          |
| `DockerFile`         | ❌ No       | Requerido para backend Flask         |
| `docker-compose.yml` | ❌ No       | Esencial para levantar todo el stack |

---

## 💡 Recomendaciones

* Mantener servicios en ejecución mientras desarrollamos.
* Configurar usuarios desde SonarQube o gestionando accesos en PostgreSQL.
* Documentar endpoints y usar `.env` para variables sensibles.



















-----------


# Flask API

## Instalación
- Crear el venv e instalar los requirements
```bash
make init
```
---

## Ejecución

- Ejecutar el servidor
```bash
make run
```

---

## Flask WTF
### Instalación
- Activar el entorno
```bash
source venv/bin/activate
```
- Instalar Flask-WTF
```bash
pip install -U Flask-WTF
```


## Docker Sonar-Scanner

> [!CAUTION]
> Si creamos contenedores, los datos que se generan por defecto, se pierden una vez se da de baja el contenedor.


Escaneo momentáneo, no guarda nada:
```bash
docker run --rm \
  -e SONAR_HOST_URL="http://172.17.0.1:9000" \
  -e SONAR_TOKEN="sqp_17499df2008fd1d84c5c570e77e422607b422e90" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

- Se necesita un directorio del lado del host, en el sistema de archivos, y otro del lado del contenedor.

```bash
docker run --rm --name sonar -p 9000:9000 \
-v /tmp/sonarqube/datos:/opt/sonarqube/data \
-v /tmp/sonarqube/logs:/opt/sonarqube/logs \
-v /tmp/sonarqube/extensiones:/opt/sonarqube/extensions
```