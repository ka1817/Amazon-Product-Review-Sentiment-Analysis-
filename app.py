import streamlit as st
import requests

# Streamlit UI
st.title("Amazon Review Sentiment Analysis")

# Input Box
user_input = st.text_area("Enter your product review:", "")

# Predict Button
if st.button("Predict Sentiment"):
    if user_input:
        response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
        if response.status_code == 200:
            result = response.json()
            st.write(f"**Sentiment:** {result['sentiment']}")
            st.write(f"**Confidence:** {result['confidence']:.2f}")
        else:
            st.write("Error: Unable to get prediction.")
    else:
        st.write("Please enter a review.")

