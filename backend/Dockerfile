FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml .

# Install uv for faster package management
RUN pip install --no-cache-dir uv

# Install dependencies using uv
RUN uv pip install --system --no-cache-dir -r pyproject.toml

# Install additional packages for PostgreSQL
RUN uv pip install --system --no-cache-dir psycopg2-binary redis

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Default command (can be overridden by docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
