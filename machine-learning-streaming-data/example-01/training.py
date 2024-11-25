from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from stream import transaction_stream

# Initialize the model and preprocessing components
model = SGDClassifier(loss="log")  # Logistic Regression with Stochastic Gradient Descent
scaler = StandardScaler()
is_scaler_fitted = False  # To check if scaler has been fitted

# Buffer to store stream data for batch processing
batch_data = []

def preprocess_data(batch):
    """Preprocess batch data: convert to DataFrame, scale, and split."""
    df = pd.DataFrame(batch)
    X = df[['amount', 'time_of_day', 'transaction_type']]
    y = df['is_fraud']
    return X, y

def train_on_stream(stream, batch_size=100):
    """Consume streaming data and incrementally train the model."""
    global is_scaler_fitted

    for transaction in stream:
        batch_data.append(transaction)

        # Process data in batches
        if len(batch_data) >= batch_size:
            # Convert batch data into DataFrame and preprocess
            X, y = preprocess_data(batch_data)
            batch_data.clear()  # Clear buffer

            # Scale the data
            if not is_scaler_fitted:
                X = scaler.fit_transform(X)
                is_scaler_fitted = True
            else:
                X = scaler.transform(X)

            # Incrementally train the model
            model.partial_fit(X, y, classes=np.array([0, 1]))
            print(f"Trained on a batch of size {batch_size}")

def evaluate_on_test_data(test_data):
    """Evaluate the model using a test dataset."""
    X_test, y_test = preprocess_data(test_data)
    X_test = scaler.transform(X_test)  # Scale test data
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy on test data: {accuracy:.2f}")

if __name__ == "__main__":
    # Simulate a test dataset
    test_data = [
        {"amount": 200, "time_of_day": 10, "transaction_type": 0, "is_fraud": 0},
        {"amount": 4000, "time_of_day": 22, "transaction_type": 1, "is_fraud": 1},
        {"amount": 50, "time_of_day": 14, "transaction_type": 0, "is_fraud": 0},
        {"amount": 3000, "time_of_day": 3, "transaction_type": 1, "is_fraud": 1},
    ]

    # Train on simulated stream
    print("Starting stream processing and training...")
    stream = transaction_stream()
    try:
        train_on_stream(stream, batch_size=50)  # Train incrementally
    except KeyboardInterrupt:
        print("\nTraining interrupted.")

    # Evaluate the model
    print("\nEvaluating the model...")
    evaluate_on_test_data(test_data)
