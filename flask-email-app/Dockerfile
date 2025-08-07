# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy requirements and app files
COPY requirements.txt .
COPY app.py .
COPY templates ./templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]