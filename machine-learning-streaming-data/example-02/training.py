from confluent_kafka import Consumer
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import json

# Kafka consumer configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'streaming_group',
    'auto.offset.reset': 'earliest'
}

# Initialize Kafka Consumer
consumer = Consumer(kafka_config)
consumer.subscribe(['transactions'])

# Model and Preprocessing
model = SGDClassifier(loss="log")  # Incremental learning model
scaler = StandardScaler()
is_scaler_fitted = False  # Track scaler fitting

# Preprocessing Function
def preprocess_data(data):
    """Preprocess data - parse JSON, scale, and split features/target."""
    df = pd.DataFrame(data)
    X = df[['amount', 'time_of_day', 'transaction_type']]  # Features
    y = df['is_fraud']  # Target
    return X, y

# Train Model on Stream
def train_on_stream():
    global is_scaler_fitted
    batch_data = []  # Buffer for batch processing

    while True:
        msg = consumer.poll(1.0)  # Poll Kafka topic
        if msg is None:
            continue
        if msg.error():
            print("Consumer error:", msg.error())
            break

        # Parse incoming message
        transaction = json.loads(msg.value().decode('utf-8'))
        batch_data.append(transaction)

        if len(batch_data) >= 100:  # Process in mini-batches
            df = pd.DataFrame(batch_data)
            batch_data = []

            X, y = preprocess_data(df)
            if not is_scaler_fitted:
                X = scaler.fit_transform(X)
                is_scaler_fitted = True
            else:
                X = scaler.transform(X)

            # Incremental training
            model.partial_fit(X, y, classes=[0, 1])
            print(f"Processed a batch, current batch size: {len(y)}")

# Evaluate the Model
def evaluate_on_stream(test_data):
    X_test, y_test = preprocess_data(test_data)
    X_test = scaler.transform(X_test)
    predictions = model.predict(X_test)
    accuracy = (predictions == y_test).mean()
    print(f"Accuracy: {accuracy}")

# Start streaming and training
try:
    train_on_stream()
except KeyboardInterrupt:
    print("Streaming stopped.")
finally:
    consumer.close()
