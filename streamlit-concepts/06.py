import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

data = pd.read_csv('USA_Housing.csv')
model = LinearRegression()

target = st.selectbox("Select the target variable", data.columns)
features = st.multiselect("Select feature(s)", data.columns)

if features:
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    st.write(f"Mean Squared Error: {mse}")
    st.write(f"R² Score: {r2}")