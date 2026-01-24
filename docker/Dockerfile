FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app/connect_hub

# Copy requirements first (for caching)
COPY Connect-Hub/requirements.txt /app/

ENV PIP_DEFAULT_TIMEOUT=100
RUN pip install -r /app/requirements.txt

# Copy the whole project
COPY Connect-Hub/ /app/

EXPOSE 8000

# Security: run as non-root
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
USER appuser

# Start Django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
