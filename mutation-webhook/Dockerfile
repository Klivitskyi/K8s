FROM python:3.11-slim
WORKDIR /app
COPY webhook.py /app/main.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8123", "--ssl-keyfile", "/certs/tls.key", "--ssl-certfile", "/certs/tls.crt"]