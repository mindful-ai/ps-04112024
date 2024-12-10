from flask import Flask, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

app = Flask(__name__)

# Load the fine-tuned model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("./finetuned_model")
tokenizer = AutoTokenizer.from_pretrained("./finetuned_model")

# Define a prediction function
def predict(text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    # Run the model on the tokenized input
    with torch.no_grad():
        outputs = model(**inputs)
    # Get the prediction (class with the highest score)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=-1).item()
    return "positive" if predicted_class == 1 else "negative"

# Define an API route for prediction
@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    prediction = predict(text)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
