import streamlit as st
import requests

st.title("Iris Flower Classifier")
st.write("Enter the flower measurements:")

sepal_length = st.number_input("Sepal Length", 0.0, 10.0, step=0.1)
sepal_width = st.number_input("Sepal Width", 0.0, 10.0, step=0.1)
petal_length = st.number_input("Petal Length", 0.0, 10.0, step=0.1)
petal_width = st.number_input("Petal Width", 0.0, 10.0, step=0.1)

if st.button("Predict"):
    url = "http://backend-service:8000/predict"  # Kubernetes Service name
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        st.success(f"Prediction: {response.json()['prediction']}")
    else:
        st.error("Error in prediction")
