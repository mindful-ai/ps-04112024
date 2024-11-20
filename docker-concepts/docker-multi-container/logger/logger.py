from flask import Flask, request
import json
import os

app = Flask(__name__)

LOG_FILE = "logs/logs.txt"

@app.route('/log', methods=['POST'])
def log_request():
    data = request.json
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(data) + '\n')
    return {"status": "logged"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
