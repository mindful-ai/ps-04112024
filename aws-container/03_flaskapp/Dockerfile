FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Set the environment variable for Flask to run in production
ENV FLASK_APP=server.py
ENV FLASK_ENV=production

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]