import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv('USA_Housing.csv')
model = LinearRegression()

target = st.selectbox("Select the target variable", data.columns)
features = st.multiselect("Select feature(s)", data.columns)


alpha = st.slider("Regularization Strength (alpha)", 0.01, 1.0, 0.1)
from sklearn.linear_model import Ridge
model = Ridge(alpha=alpha)

if features:
    model.fit(X, y)
    st.write("Model retrained with alpha =", alpha)

if features:
    importance = model.coef_
    plt.figure()
    plt.barh(features, importance)
    st.pyplot(plt)
