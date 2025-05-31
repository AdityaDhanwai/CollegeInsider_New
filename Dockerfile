# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and app files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Flask port
EXPOSE 5000

# Start the Flask server
CMD ["python", "main.py"]