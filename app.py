import streamlit as st
import joblib
import requests
import json

# Page configuration
st.set_page_config(page_title="Deciphering Central Banks - Text Analysis", layout="centered")

# Title and description
st.title("Deciphering Central Banks - Text Analysis")
st.markdown("""
Welcome to the **Deciphering Central Banks** analysis tool!  
This app allows you to input text and run **Sentiment Analysis** and **Agent Words Detection**.
""")

# Define the API URL
api_url = "https://WE NEED YOU HUGO"

# Load pre-trained models
@st.cache_data(allow_output_mutation=True)
def load_model(model_path):
    return joblib.load(model_path)

# Load models
sentiment_model_path = "COME ON BESS"
agent_model_path = "COME ON BESS"

sentiment_model = load_model(sentiment_model_path)
agent_model = load_model(agent_model_path)

# Users input text box
st.subheader("Text to Analyse")
user_text = st.text_area("Write or paste the text you want to analyse:", height=200)

# Function for Sentiment Analysis
def predict_sentiment(text, model):
    prediction = model.predict([text])[0]
    return "Positive" if prediction == 1 else "Negative"

# Function for Agent Words Detection
def detect_agent_words(text, model):
    prediction = model.predict([text])[0]
    return "Detected" if prediction == 1 else "Not Detected"

# Function to call API
def call_api(api_url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get a response from the API"}

# Analyse button
if st.button("Analyse Text"):
    if user_text:
        sentiment_result = predict_sentiment(user_text, sentiment_model)
        st.markdown(f"**Sentiment Analysis Result:** {sentiment_result}")
        
        agent_result = detect_agent_words(user_text, agent_model)
        st.markdown(f"**Agent Words Detection Result:** {agent_result}")

    else:
        st.warning("Please input some text for analysis.")

# Footer
st.markdown("---")
st.markdown("**Created by [The Bess Team] - Deciphering Central Banks Project**")
