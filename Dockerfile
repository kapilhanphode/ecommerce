FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# collect static for admin
#RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]