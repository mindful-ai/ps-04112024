import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import os

def main():
    # Load dataset
    data_path = os.path.join(os.path.dirname(__file__), "data/housing.csv")
    data = pd.read_csv(data_path)

    # Define features and target
    X = data[["latitude", "longitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households", "median_income"]]
    y = data["median_house_value"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    predictions = model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    print(f"Model RMSE: {rmse}")

    # Save the model
    model_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, "model.pkl"))

if __name__ == "__main__":
    main()
