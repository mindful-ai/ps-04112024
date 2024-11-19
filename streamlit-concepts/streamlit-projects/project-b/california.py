import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Calculate model performance
mse = mean_squared_error(y_test, model.predict(X_test))

# Streamlit app
st.title("California House Price Prediction")

st.write("""
This app uses a machine learning model to predict California house prices based on input features.
Please enter the values below to get a predicted house price.
""")

# User inputs
MedInc = st.number_input("Median Income in Block ($10,000s)", min_value=0.5, max_value=15.0, step=0.1)
HouseAge = st.slider("House Age (Years)", 1, 52, 25)
AveRooms = st.number_input("Average Number of Rooms", min_value=2.0, max_value=10.0, step=0.1)
AveBedrms = st.number_input("Average Number of Bedrooms", min_value=1.0, max_value=5.0, step=0.1)
Population = st.number_input("Block Population", min_value=1, max_value=3500, step=10)
AveOccup = st.number_input("Average Occupancy", min_value=1.0, max_value=6.0, step=0.1)
Latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, step=0.1)
Longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0, step=0.1)

# Prepare input data
input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])

# Predict house price
if st.button("Predict House Price"):
    prediction = model.predict(input_data)
    st.write(f"Predicted House Price: ${prediction[0] * 100000:.2f}")
    st.write(f"Model Mean Squared Error on Test Data: {mse:.2f}")
