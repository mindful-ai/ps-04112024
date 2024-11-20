from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

MODEL_SERVING_URL = "http://model_serving:5001/predict"

@app.post("/predict")
async def get_prediction(features: list):
    try:
        response = requests.post(MODEL_SERVING_URL, json={"features": features})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
