import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import numpy as np

# Generate a sample dataset (for demonstration)
# Uncomment the following lines to create and save a sample CSV
# df = pd.DataFrame({
#     'Age': np.random.randint(20, 60, size=500),
#     'Salary': np.random.randint(30000, 100000, size=500),
#     'Gender': np.random.choice(['Male', 'Female'], size=500),
#     'Approved': np.random.choice([0, 1], size=500)  # Target
# })
# df.to_csv("loan_data.csv", index=False)

# Batch size for incremental learning
BATCH_SIZE = 100

# Initialize necessary components
scaler = StandardScaler()
encoder = LabelEncoder()
model = SGDClassifier(loss="log")  # Stochastic Gradient Descent for binary classification

# Custom preprocessing function
def preprocess_data(df):
    # Encode categorical features
    df['Gender'] = encoder.fit_transform(df['Gender'])  # Male=1, Female=0
    # Extract features and target
    X = df[['Age', 'Salary', 'Gender']]
    y = df['Approved']
    return X, y

# Read and process data in batches
def train_in_batches(file_path):
    chunks = pd.read_csv(file_path, chunksize=BATCH_SIZE)  # Read in batches
    for chunk in chunks:
        X, y = preprocess_data(chunk)
        # Scale features
        X_scaled = scaler.fit_transform(X)
        # Incremental learning
        model.partial_fit(X_scaled, y, classes=np.array([0, 1]))  # Provide classes for first batch

# Evaluate the model
def evaluate(file_path):
    chunks = pd.read_csv(file_path, chunksize=BATCH_SIZE)
    y_true, y_pred = [], []
    for chunk in chunks:
        X, y = preprocess_data(chunk)
        X_scaled = scaler.transform(X)  # Use transform, not fit_transform
        y_true.extend(y)
        y_pred.extend(model.predict(X_scaled))
    print("Accuracy:", accuracy_score(y_true, y_pred))

# Train the model
train_file = "loan_data.csv"  # Path to the dataset
train_in_batches(train_file)

# Evaluate the model
evaluate(train_file)
