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