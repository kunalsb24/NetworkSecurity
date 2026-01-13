FROM python:3.10-slim-bookworm

WORKDIR /app

COPY . /app

# Install awscli + system deps
RUN apt-get update \
    && apt-get install -y --no-install-recommends awscli \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
