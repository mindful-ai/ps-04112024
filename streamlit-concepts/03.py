import pandas as pd
import streamlit as st

st.title("Upload Data for EDA")
file = st.file_uploader("Upload a CSV file", type="csv")
if file:
    data = pd.read_csv(file)
    st.write("Data Preview:", data.head())
    st.write("Basic Statistics:", data.describe())

'''

This app lets users upload a dataset and displays the first few rows and summary statistics. 
It introduces st.file_uploader() for file handling and st.write() for data display.
'''