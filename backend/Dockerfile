# Dockerfile para backend Flask
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del backend
COPY . .

# Especificar el puerto expuesto (coincidir con docker-compose)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "run.py"]
