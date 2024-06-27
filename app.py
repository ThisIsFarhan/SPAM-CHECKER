import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Load model from file
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Load the CountVectorizer object from the file
with open('count_vectorizer.pkl', 'rb') as file:
    loaded_cv = pickle.load(file)

st.title("SPAM MESSAGE CHECKER")
st.write("Developed and Deployed by Farhan Ali Khan")

text = st.text_input("Enter the text to check")
btn = st.button("CHECK")

if btn:
    textsList = []
    textsList.append(text)
    textsList_vector = loaded_cv.transform(textsList)
    predictions = loaded_model.predict(textsList_vector)

    if predictions[0] == 1:
        st.subheader("Text is Spam")
    else:
        st.subheader("Text is not Spam")