#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput

# gunicorn config.wsgi:application --bind 0.0.0.0:8000
# celery -A config.settings.celery worker -l info
python manage.py runserver 0.0.0.0:8000
