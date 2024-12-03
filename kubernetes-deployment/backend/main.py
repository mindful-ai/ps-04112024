from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load pre-trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(input_data: PredictionInput):
    data = [[
        input_data.sepal_length,
        input_data.sepal_width,
        input_data.petal_length,
        input_data.petal_width
    ]]
    prediction = model.predict(data)[0]
    return {"prediction": prediction}
