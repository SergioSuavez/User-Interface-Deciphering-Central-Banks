import streamlit as st
import requests
import json
import pandas as pd

# Set up page configuration
st.set_page_config(page_title="Deciphering Central Banks - Text & URL Analysis", layout="centered", page_icon="📊")

# Title and description
st.title("Deciphering Central Banks - Text & URL Analysis")
st.markdown("""
Welcome to the **Deciphering Central Banks** analysis tool!  
This app allows you to input text or a URL to run **Sentiment Analysis** and **Agent Words Detection**.
The agents could be households, firms, the financial sector, governments, or central banks.
""")

# Define the API URL
api_url = "https://WE NEED YOU HUGO"

# Input section
st.subheader("Input for Analysis")
input_type = st.radio("Choose input type:", ("Text", "URL"))

user_input = None
if input_type == "Text":
    user_input = st.text_area("Paste the text you want to analyze:", height=200)
else:
    user_input = st.text_input("Paste the URL you want to analyze:")

# Analyse button
if st.button("Analyze"):
    if user_input:
        # Send request to the API
        data = {"input": user_input, "type": input_type.lower()}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(api_url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                # Response from the API
                result = response.json()
                text_fragments = result.get("text_fragments", [])
                sentiments = result.get("sentiments", [])
                agents = result.get("agents", [])
                
                # Create a DataFrame for displaying results in a table format
                df = pd.DataFrame({
                    "Text": text_fragments,
                    "Agent": agents,
                    "Sentiment": sentiments
                })

                # Display table of results
                st.markdown("### Analysis Results")
                st.dataframe(df)

            else:
                st.error("Error: Could not retrieve results from the API.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please input some text or a URL for analysis.")

# Footer
st.markdown("---")
st.markdown("**Created by The Bess Team - Deciphering Central Banks Project**")
