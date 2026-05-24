import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📘 Student Score Predictor")

st.write("Enter study hours to predict exam score.")

hours = st.slider("Study Hours", 1, 12, 5)

if st.button("Predict Score"):
    prediction = model.predict(np.array([[hours]]))

    st.success(f"Predicted Score: {prediction[0]:.2f}")