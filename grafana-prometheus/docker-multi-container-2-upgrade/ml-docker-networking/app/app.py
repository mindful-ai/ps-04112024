# Flask backend script

from flask import Flask, request, jsonify, Response
import redis
import pickle
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Define a Prometheus counter
request_counter = Counter('flask_app_requests_total', 'Total requests to Flask app')

@app.route('/')
def home():
    return "Hello, Flask with Prometheus!"

# Expose metrics endpoint
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

# Connect to Redis
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

# Load the model
with open("../models/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["GET"])
def predict():
    # Retrieve features from request
    features = request.args
    try:
        data = [[float(features.get(key)) for key in sorted(features.keys())]]
        prediction = model.predict(data)[0]
        request_counter.inc()  # Increment the counter
        # Log prediction in Redis
        redis_client.set("latest_prediction", prediction)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"prediction": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



