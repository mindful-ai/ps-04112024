# Create an account here: https://openweathermap.org/api

import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
import os

# Set your API keys here
os.environ["OPENAI_API_KEY"] = "sk-your-openai-api-key"
os.environ["OPENWEATHERMAP_API_KEY"] = "your-openweathermap-api-key"

# Initialize LLM and tools outside the Streamlit app function to avoid reinitializing on each interaction
llm = OpenAI(temperature=0)
tools = load_tools(["openweathermap-api"], llm)
weather_agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Streamlit app starts here
def run_weather_app():
    st.title('Weather Forecast')
    city = st.text_input('Enter a city name:', '')
    if st.button('Get Weather'):
        # Generating a query dynamically based on user input
        query = f"What's the weather in {city} in the next 3 hours?"
        # Getting the weather report
        report = weather_agent.run(query)
        # Displaying the report
        st.text(report)

# This is the main app function call
if __name__ == '__main__':
    run_weather_app()