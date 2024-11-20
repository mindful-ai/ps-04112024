import os

def create_project_structure(base_dir):
    # Define the directory structure
    structure = {
        "ml-flask-app": {
            "app": {
                "static": {
                    "styles.css": "body { font-family: Arial; } /* Add your CSS here */"
                },
                "templates": {
                    "home.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <title>House Price Prediction</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Predict California House Prices</h1>
    <form action="/predict" method="post">
        <label>Median Income:</label>
        <input type="text" name="MedInc" required><br>
        <label>House Age:</label>
        <input type="text" name="HouseAge" required><br>
        <label>Average Rooms:</label>
        <input type="text" name="AveRooms" required><br>
        <label>Average Bedrooms:</label>
        <input type="text" name="AveBedrms" required><br>
        <label>Population:</label>
        <input type="text" name="Population" required><br>
        <label>Average Occupancy:</label>
        <input type="text" name="AveOccup" required><br>
        <label>Latitude:</label>
        <input type="text" name="Latitude" required><br>
        <label>Longitude:</label>
        <input type="text" name="Longitude" required><br>
        <button type="submit">Predict</button>
    </form>
</body>
</html>""",
                    "result.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <title>Prediction Result</title>
</head>
<body>
    <h1>Prediction Result</h1>
    <p>The predicted house price is: ${{ prediction }}</p>
</body>
</html>"""
                },
                "app.py": """from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the form
    features = [
        float(request.form['MedInc']),
        float(request.form['HouseAge']),
        float(request.form['AveRooms']),
        float(request.form['AveBedrms']),
        float(request.form['Population']),
        float(request.form['AveOccup']),
        float(request.form['Latitude']),
        float(request.form['Longitude']),
    ]
    prediction = model.predict([features])[0]
    return render_template("result.html", prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
"""
                },
                "requirements.txt": "flask==2.3.0\nnumpy==1.23.0\nscikit-learn==1.3.1\n",
                "Dockerfile": """FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]"""
            },
            "data": {
                "california_housing.csv": "Placeholder for California housing dataset (optional)"
            },
            "model_training": {
                "train_model.py": """import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

data = fetch_california_housing(as_frame=True)
df = data.frame

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

with open("../app/model.pkl", "wb") as f:
    pickle.dump(model, f)""",
                "requirements.txt": "scikit-learn==1.3.1\npandas==2.1.1\n"
            },
            "docker-compose.yml": """version: "3.9"

services:
  flask-app:
    build:
      context: ./app
    ports:
      - "5000:5000"
    volumes:
      - app-data:/app
    environment:
      - FLASK_ENV=development
    restart: always

volumes:
  app-data:
"""
        }


    def create_files(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(path, content)
            else:
                with open(path, "w") as f:
                    f.write(content)

    create_files(base_dir, structure)


# Specify the base directory and generate the structure
base_directory = "ml-flask-app"
create_project_structure(base_directory)
print(f"Project structure created under '{base_directory}'")
