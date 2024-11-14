from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "../models/model.pkl")
model = joblib.load(model_path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get input data
            input_data = [
                float(request.form["latitude"]),
                float(request.form["longitude"]),
                float(request.form["housing_median_age"]),
                float(request.form["total_rooms"]),
                float(request.form["total_bedrooms"]),
                float(request.form["population"]),
                float(request.form["households"]),
                float(request.form["median_income"]),
            ]
            
            # Make prediction
            prediction = model.predict([input_data])[0]
            return render_template("index.html", prediction=round(prediction, 2))
        except ValueError:
            return "Please enter valid data."
    
    return render_template("index.html", prediction=None)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
