# Dockerfile for Python client that can connect to CARLA server
# This solves the macOS compatibility issue by running client in Linux container

FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and install CARLA Python API
RUN mkdir -p /tmp/carla && cd /tmp/carla && \
    wget https://carla-releases.s3.us-east-005.backblazeb2.com/Linux/CARLA_0.9.15.tar.gz && \
    tar -xzf CARLA_0.9.15.tar.gz PythonAPI/carla/dist/carla-0.9.15-py3.7-linux-x86_64.egg && \
    unzip -q PythonAPI/carla/dist/carla-0.9.15-py3.7-linux-x86_64.egg -d /tmp/carla_pkg && \
    cp -r /tmp/carla_pkg/carla /usr/local/lib/python3.9/site-packages/ && \
    rm -rf /tmp/carla

# Copy project requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the autonomy stack code
COPY carla_robust_autonomy_stack /app/carla_robust_autonomy_stack
COPY scripts /app/scripts

# Default command: run CLI
CMD ["python", "-m", "carla_robust_autonomy_stack.cli", "--help"]
