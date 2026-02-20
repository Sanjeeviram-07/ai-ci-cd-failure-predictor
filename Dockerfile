# Dockerfile
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default command (run prediction)
CMD ["python", "src/predict.py"]