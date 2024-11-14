import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

st.title("Housing Price Prediction")

# Input fields for user to enter data
latitude = st.number_input("Latitude", format="%.6f")
longitude = st.number_input("Longitude", format="%.6f")
housing_median_age = st.number_input("Housing Median Age", format="%.1f")
total_rooms = st.number_input("Total Rooms", format="%d")
total_bedrooms = st.number_input("Total Bedrooms", format="%d")
population = st.number_input("Population", format="%d")
households = st.number_input("Households", format="%d")
median_income = st.number_input("Median Income", format="%.2f")

# Button for prediction
if st.button("Predict Housing Price"):
    # Make prediction
    input_data = np.array([[latitude, longitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income]])
    prediction = model.predict(input_data)
    st.write(f"Predicted Housing Price: ${prediction[0]:,.2f}")
