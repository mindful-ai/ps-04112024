from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    #return jsonify({"message": "Hello, Docker Volumes with Flask!"})
    return "<h1>Hello, Docker Volumes with Flask!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
