# Use Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files (will use STATIC_ROOT)
RUN python backend/manage.py collectstatic --noinput

# Expose port (Fly will route to this)
EXPOSE 8080

# Start Gunicorn - note: backend.backend.wsgi is your WSGI module
CMD ["gunicorn", "backend.backend.wsgi:application", "--bind", "0.0.0.0:8080"]