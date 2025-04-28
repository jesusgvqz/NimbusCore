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


## Docker Sonar-Scanner

```bash
docker run --rm \
  -e SONAR_HOST_URL="http://172.17.0.1:9000" \
  -e SONAR_TOKEN="sqp_17499df2008fd1d84c5c570e77e422607b422e90" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli

```

