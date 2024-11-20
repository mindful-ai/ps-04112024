# Use the official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose the Flask app's port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
