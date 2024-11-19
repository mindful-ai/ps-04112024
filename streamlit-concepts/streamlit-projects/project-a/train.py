import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("housing.csv")

# Define features and target
X = data[["latitude", "longitude", "housing_median_age", "total_rooms", "total_bedrooms", 
          "population", "households", "median_income"]]
y = data["median_house_value"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.pkl")
print("Model trained and saved as model.pkl")
