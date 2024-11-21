# Flask backend script

from flask import Flask, request, jsonify
import redis
import pickle

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

# Load the model
with open("/models/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["GET"])
def predict():
    # Retrieve features from request
    features = request.args
    try:
        data = [[float(features.get(key)) for key in sorted(features.keys())]]
        prediction = model.predict(data)[0]
        
        # Log prediction in Redis
        redis_client.set("latest_prediction", prediction)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
