from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

app = FastAPI()

# Define a Pydantic model for request data validation
class HouseData(BaseModel):
    latitude: float
    longitude: float
    housing_median_age: float
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float

@app.post("/predict")
def predict(data: HouseData):
    # Prepare the data for prediction
    input_data = np.array([[data.latitude, data.longitude, data.housing_median_age, 
                            data.total_rooms, data.total_bedrooms, data.population, 
                            data.households, data.median_income]])

    # Make a prediction
    try:
        prediction = model.predict(input_data)[0]
        return {"Predicted Housing Price": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
