FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiamos requirements primero (aprovecha cache de Docker)
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiamos todo el código Django
COPY . .

# Generamos los archivos estáticos durante el build
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# En producción usamos gunicorn, no runserver.
# Ejecutamos migrate al arrancar el contenedor y luego levantamos el servidor.
CMD python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}