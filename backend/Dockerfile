# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-client \
    iputils-ping \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x app/run.sh

RUN useradd -m -s /bin/bash nimbuscore

RUN mkdir -p /home/nimbuscore/.ssh && \
    chown -R nimbuscore:nimbuscore /home/nimbuscore/.ssh && \
    chmod 700 /home/nimbuscore/.ssh

RUN chown -R nimbuscore:nimbuscore /app

USER nimbuscore

CMD ["./run.sh"]

# para producción
# CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]

# para desarrollo
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
