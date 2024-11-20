import streamlit as st
import requests

BACKEND_URL = "http://backend:5002/predict"

st.title("Machine Learning Prediction App")

features = st.text_input("Enter features (comma-separated)", "")
if st.button("Predict"):
    try:
        features_list = [float(x.strip()) for x in features.split(",")]
        response = requests.post(BACKEND_URL, json={"features": features_list})
        prediction = response.json()['prediction']
        st.success(f"Prediction: {prediction}")
    except Exception as e:
        st.error(f"Error: {e}")
