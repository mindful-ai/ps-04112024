# Worker script to log predictions

import redis
import time

# Connect to Redis
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

while True:
    prediction = redis_client.get("latest_prediction")
    if prediction:
        with open("/logs/predictions.log", "a") as log_file:
            log_file.write(f"Prediction logged: {prediction}\n")
    time.sleep(5)  # Log every 5 seconds
