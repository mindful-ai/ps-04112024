'''
This basic app displays a static prediction from a linear regression model. 
It introduces the layout with st.title() and st.write() to output text and data.
'''


import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Simple model
model = LinearRegression()
model.fit([[1], [2], [3]], [2, 4, 6])

st.title("Simple ML Model Prediction")
x = 5
prediction = model.predict([[x]])
st.write(f"Prediction for {x}: {prediction[0]}")
