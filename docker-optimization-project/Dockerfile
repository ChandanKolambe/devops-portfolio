# STAGE 1: Build environment
FROM python:3.8-slim as builder

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# STAGE 2: Production image
FROM python:3.8-slim

# Security: Create non-root user
RUN groupadd -r flask && useradd -r -g flask flask \
    && mkdir /app && chown flask:flask /app

# Copy virtual env from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app
COPY --chown=flask:flask ./app .

# Switch to non-root user
USER flask

# Expose port and run
EXPOSE 5000
CMD ["python", "app.py"]