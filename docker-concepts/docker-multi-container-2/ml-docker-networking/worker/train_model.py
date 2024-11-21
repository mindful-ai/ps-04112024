# Script to train and save the model

import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load California Housing dataset
data = fetch_california_housing(as_frame=True)
X = data.data
y = data.target

# Train-test split and model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model
with open("/models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved to /models/model.pkl")
