#!/usr/bin/env bash

# Esperamos a que la base de datos esté lista
sleep 10

# Migraciones
python -u manage.py makemigrations
python -u manage.py migrate
python manage.py collectstatic --noinput

# Ejecutamos el servidor de aplicaciones (Gunicorn)
gunicorn --bind 0.0.0.0:8000 core.wsgi:application --reload
