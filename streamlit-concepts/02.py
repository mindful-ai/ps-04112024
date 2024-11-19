
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Simple model
model = LinearRegression()
model.fit([[1], [2], [3]], [2, 4, 6])

x_input = st.number_input("Enter a value for prediction:", value=5)
prediction = model.predict([[x_input]])
st.write(f"Prediction: {prediction[0]}")


from sklearn.metrics import mean_squared_error, r2_score


