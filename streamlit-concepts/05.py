import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

data = pd.read_csv('USA_Housing.csv')
model = LinearRegression()

target = st.selectbox("Select the target variable", data.columns)
features = st.multiselect("Select feature(s)", data.columns)

if features:
    X = data[features]
    y = data[target]
    model.fit(X, y)
    st.write("Model trained successfully")

'''
This adds a model training section, allowing users to select features and a target 
variable. st.multiselect() enables users to choose multiple features.

'''

