import requests
import streamlit as st


def predict_api(input_value):
    url = "http://localhost:8000/predict"
    response = requests.post(url, json={"input": input_value})
    return response.json()

x_input = st.number_input("Enter value for prediction")
if st.button("Get Prediction from API"):
    result = predict_api(x_input)
    st.write("Prediction from API:", result)


'''
This example demonstrates using an API endpoint to retrieve predictions, 
illustrating how Streamlit apps can integrate with external services or deployed models.


'''