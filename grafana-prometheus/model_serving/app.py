from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Counter, Summary
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# Create Prometheus metrics
REQUEST_COUNT = Counter('model_request_count', 'Total number of model prediction requests')
PREDICTION_LATENCY = Summary('model_prediction_latency_seconds', 'Time taken to serve a model prediction')

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Expose /metrics endpoint for Prometheus
@app.route('/metrics')
def metrics():
    from prometheus_client import generate_latest
    return generate_latest()

@app.route('/predict', methods=['POST'])
@PREDICTION_LATENCY.time()  # Measure prediction latency
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)  # Reshape for single prediction
    
    # Validate the input
    if features.shape[1] != 8:
        return jsonify({'error': 'Invalid input: California Housing dataset expects 8 features'}), 400
    
    # Increment request count
    REQUEST_COUNT.inc()

    # Make prediction
    prediction = model.predict(features)[0]
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5001)
