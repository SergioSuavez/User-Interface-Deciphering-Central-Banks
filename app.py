import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(page_title="Deciphering Central Banks - Text Analysis", layout="centered", page_icon="📊")

# Title and description
st.title("Deciphering Central Banks - Text Analysis")
st.markdown("""
Welcome to the **Deciphering Central Banks** analysis tool!  
This app allows you to input text and run **Sentiment Analysis** and **Agent Words Detection**.
""")

# Define the API URL
api_url = "https://WE NEED YOU HUGO"

# Users input text box
st.subheader("Text to Analyse")
user_text = st.text_area("Write or paste the text you want to analyse:", height=200)

# Analyse button
if st.button("Analyze Text"):
    if user_text:
        # Request the API
        data = {"text": user_text}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(api_url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                # Response from the API
                result = response.json()
                sentiment = result.get("sentiment", "N/A")
                agent_detection = result.get("agent_detection", "N/A")

                # Results
                st.markdown("### Analysis Results")
                st.markdown(f"**Sentiment Analysis:** {sentiment}")
                st.markdown(f"**Agent Words Detection:** {agent_detection}")
            else:
                st.error("Error: Could not retrieve results from the API.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please input some text for analysis.")

# Footer
st.markdown("---")
st.markdown("**Created by [The Bess Team] - Deciphering Central Banks Project**")
