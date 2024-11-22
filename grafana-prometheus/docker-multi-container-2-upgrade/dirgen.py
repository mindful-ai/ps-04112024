import os

# Define the directory structure
structure = {
    "ml-docker-networking": {
        "app": {
            "app.py": "# Flask backend script",
            "requirements.txt": "flask\nredis\nscikit-learn",
        },
        "worker": {
            "generate_predictions.py": "# Worker script to log predictions",
            "train_model.py": "# Script to train and save the model",
            "requirements.txt": "redis\nscikit-learn",
        },
        "frontend": {
            "app.py": "# Streamlit frontend script",
            "requirements.txt": "streamlit\nrequests",
        },
        "logs": {},  # Directory for logs
        "models": {},  # Directory for models
        "docker-compose.yml": """version: "3.9"

services:
  flask_app:
    build: ./app
    container_name: flask_app
    ports:
      - "5000:5000"
    networks:
      - ml_network
    volumes:
      - ./models:/models

  redis:
    image: redis:alpine
    container_name: redis
    networks:
      - ml_network
    volumes:
      - redis_data:/data

  worker:
    build: ./worker
    container_name: worker
    networks:
      - ml_network
    depends_on:
      - redis
    volumes:
      - ./logs:/logs
      - ./models:/models

  frontend:
    build: ./frontend
    container_name: streamlit_frontend
    ports:
      - "8501:8501"
    networks:
      - ml_network
    depends_on:
      - flask_app

  busybox:
    image: busybox
    container_name: busybox_logger
    command: tail -f /logs/predictions.log
    networks:
      - ml_network
    depends_on:
      - worker
    volumes:
      - ./logs:/logs

volumes:
  redis_data:
  logs:
  models:

networks:
  ml_network:
    driver: bridge
""",
    },
}

# Function to create directory structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # It's a subdirectory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:  # It's a file
            with open(path, "w") as f:
                f.write(content)

# Generate the structure
base_dir = "ml-docker-networking"
create_structure("", structure)
print(f"Directory structure for '{base_dir}' has been created successfully!")
