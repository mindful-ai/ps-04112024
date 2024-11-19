import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

if file:
    st.title("Data Visualization")
    feature = st.selectbox("Select a feature to visualize", data.columns)
    plt.figure()
    sns.histplot(data[feature], kde=True)
    st.pyplot(plt)

'''

Here, st.selectbox() allows users to select features to visualize. 
st.pyplot() displays Seaborn plots, adding visual insight to the EDA process.



'''