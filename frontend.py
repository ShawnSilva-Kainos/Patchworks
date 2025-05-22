import streamlit as st
from backend import api_response, api_response_symptoms


# Streamlit app

st.title("Analyse your image")

# User input for URL
url_input = st.text_input("Enter a URL of your image:")
symptoms = st.text_input("Enter the symptoms you are experiencing:")
# Button to trigger API call
if st.button("Analyse"):
    if url_input:
        if symptoms:
            try:
                response = api_response_symptoms(url_input, symptoms)
                # Display the image and response
                st.image(url_input)
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            try:
                response = api_response(url_input)
                st.image(url_input)
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a URL before submitting.")
