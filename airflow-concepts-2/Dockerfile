# Base Airflow image
FROM apache/airflow:2.7.1

# Install additional Python packages
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Set the working directory
WORKDIR /opt/airflow

# Expose ports for the Airflow webserver
EXPOSE 8080
