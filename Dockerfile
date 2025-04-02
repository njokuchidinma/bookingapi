FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "bookingapi.wsgi:application", "--bind", "0.0.0.0:8000"]
