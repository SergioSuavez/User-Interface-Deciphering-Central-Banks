import streamlit as st
import requests
import json
import pandas as pd
from PIL import Image

# Page configuration
st.set_page_config(page_title="Deciphering Central Banks - Text & URL Analysis", layout="centered", page_icon="📊")

# CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2F2F2F;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 36px;
        color: #FFFFFF;
    }
    .description {
        text-align: center;
        font-size: 18px;
        color: #D3D3D3;
    }
    .sidebar .sidebar-content {
        background-color: #404040;
        color: #FFFFFF;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
        text-align: center;
    }
    .css-1d391kg {
        padding: 10px;
    }
    h2, h3, h4 {
        color: #D3D3D3;
    }
    .stButton>button {
        background-color: #808080;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #A9A9A9;
    }
    .dataframe {
        background-color: #333333;
        color: #FFFFFF;
    }
    .footer {
        background-color: #404040;
        color: white;
        text-align: center;
        padding: 10px;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo
try:
    small_logo = Image.open("Resources/DALL.E_Logo_NoBKG.png")
    st.sidebar.image(small_logo, use_column_width=False, width=120)
except FileNotFoundError:
    st.sidebar.warning("Small logo not found. Please ensure the image is in the correct path.")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "FAQs", "About"])

# API URL
api_url = "https://deciphering-cb-image-681020458300.europe-west1.run.app/docs"

# Pages
if page == "Home":
    # Banner
    try:
        header_image = Image.open("Resources/DALL.E_Banner.jpg")
        st.image(header_image, use_column_width=True)
    except FileNotFoundError:
        st.warning("Header image not found. Please make sure the image is in the correct path.")
    
    # Title and Description
    st.markdown("<h1 class='title'>Deciphering Central Banks</h1>", unsafe_allow_html=True)
    st.markdown("<p class='description'>Text & URL Analysis Tool for Sentiment and Agent Words Detection</p>", unsafe_allow_html=True)

    st.markdown("""
    Welcome to the **Deciphering Central Banks** analysis tool!  
    This app allows you to input text or a URL to run **Sentiment Analysis** and **Agent Words Detection**.
    The agents could be households, firms, the financial sector, governments, or central banks.
    """)

    # Users choice of input
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

                    # DataFrame for displaying results in a table
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

# FAQs page
elif page == "FAQs":
    # Banner
    try:
        banner_image = Image.open("Resources/DALL.E_Banner.jpg")  # Replace with your own banner image path
        st.image(banner_image, use_column_width=True)
    except FileNotFoundError:
        st.warning("Banner image not found. Please ensure the image is in the correct path.")
    # Content
    st.subheader("Frequently Asked Questions")
    st.markdown("""
    **Q: What is Sentiment Analysis?**  
    A: Sentiment Analysis determines the emotional tone behind a body of text, helping to understand opinions, attitudes, and emotions.

    **Q: What are Agent Words?**  
    A: Agent words in this context refer to entities such as households, firms, the financial sector, governments, or central banks identified within the text.

    **Q: What kind of text or URL can I input?**  
    A: You can input any text or URL that contains data related to central banks, financial markets, economic analysis, or similar topics.

    **Q: How is the sentiment score calculated?**  
    A: The sentiment score is calculated based on the analysis of text fragments using natural language processing algorithms.

    **Q: Can I analyze documents in languages other than English?**  
    A: Currently, the analysis is optimized for English text. Support for other languages may be added in future versions.
    """)

# About page
elif page == "About":
    # Banner
    try:
        banner_image = Image.open("Resources/DALL.E_Banner.jpg")
        st.image(banner_image, use_column_width=True)
    except FileNotFoundError:
        st.warning("Banner image not found. Please ensure the image is in the correct path.")
    # Content
    st.subheader("About This Project")
    st.markdown("""
    **Deciphering Central Banks** is an innovative project aimed at using natural language processing (NLP) to analyze communications from central banks and other financial institutions.
    
    By detecting sentiment and identifying agent words in various texts, we hope to better understand the narratives and insights provided by these institutions.
    
    This tool was developed by **The Bess Team** as part of our efforts to enhance transparency and understanding in the financial sector.
    
    **Team Members:**  
    - Sasha Bessarabova  
    - Sergio Suarez  
    - Hugo Rao  
    - Sébastien Barbieux
    """)

# Footer
st.markdown(
    """
    <div class='footer'>
        <p>Deciphering Central Banks Project - Created by The Bess Team</p>
    </div>
    """,
    unsafe_allow_html=True
)
