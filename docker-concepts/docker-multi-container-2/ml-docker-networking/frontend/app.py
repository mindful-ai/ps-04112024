# Streamlit frontend script

import streamlit as st
import requests

st.title("California Housing Price Prediction")

st.sidebar.header("Input Features")
features = {
    "MedInc": st.sidebar.slider("Median Income", 1.0, 15.0, 5.0),
    "HouseAge": st.sidebar.slider("House Age", 1, 50, 20),
    "AveRooms": st.sidebar.slider("Average Rooms", 2.0, 10.0, 6.0),
    "AveBedrms": st.sidebar.slider("Average Bedrooms", 1.0, 5.0, 2.0),
    "Population": st.sidebar.slider("Population", 200, 5000, 1500),
    "AveOccup": st.sidebar.slider("Average Occupancy", 1.0, 5.0, 3.0),
    "Latitude": st.sidebar.slider("Latitude", 32.0, 42.0, 35.0),
    "Longitude": st.sidebar.slider("Longitude", -124.0, -114.0, -120.0),
}

if st.button("Predict"):
    response = requests.get("http://flask_app:5000/predict", params=features)
    if response.status_code == 200:
        st.success(f"Prediction: {response.json()['prediction']}")
    else:
        st.error("Prediction failed!")
