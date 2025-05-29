# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x app/run.sh

CMD ["./run.sh"]

# para producción
# CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]

# para desarrollo
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
