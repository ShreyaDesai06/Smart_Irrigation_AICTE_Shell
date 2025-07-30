import streamlit as st
import numpy as np
import joblib

# Load model only once
@st.cache_resource
def load_model():
    return joblib.load("Farm_Irrigation_System.pkl")

model = load_model()

# Page configuration
st.set_page_config(page_title="Smart Sprinkler System", layout="centered")

# --- Title and subtitle ---
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>💧 Smart Irrigation & Sprinkler Controller</h1>",
    unsafe_allow_html=True

)
st.markdown(
    "<p style='text-align: center; font-size:16px;'>An AI-powered irrigation solution for precision farming</p>",
    unsafe_allow_html=True
)
st.markdown("---")

# --- Sensor Input Section ---
st.markdown(
    "<h3 style='color: #2E86C1;'>🌾 Sensor Input Panel</h3>"
    "<p style='font-size:15px;'>Provide scaled sensor values (0.0 to 1.0) to simulate real-time field conditions and control sprinkler activity.</p>",
    unsafe_allow_html=True
)


sensor_values = []
for i in range(20):
    st.markdown(
        f"<span style='font-weight:600; font-size:15px; color:#1f77b4;'>🔧 Sensor {i}</span>",
        unsafe_allow_html=True
    )
    val = st.slider("", 0.0, 1.0, 0.5, 0.01, key=f"sensor_{i}")
    sensor_values.append(val)
    st.markdown("<div style='height:2px; background-color:#eee; margin:5px 0 10px 0;'></div>", unsafe_allow_html=True)

# --- Predict Button ---
if st.button("🔍 Predict Sprinkler Status"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("---")
    st.markdown(
        "<h3 style='color: #27AE60;'>🌱 Prediction Results</h3>"
        "<p style='font-size:15px;'>Each sprinkler's status based on input sensor data:</p>",
        unsafe_allow_html=True
    )

    for i, status in enumerate(prediction):
        st.success(f"Sprinkler {i} (parcel_{i}): {'🟢 ON' if status == 1 else '🔴 OFF'}")

# --- Footer ---
# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align:center; padding-top:10px;'>"
    "<p style='font-size:14px; color:gray;'>Created and submitted by <strong>Shreya</strong></p>"
    "<p style='font-size:13px; color:#888;'>This project is part of the <strong>AICTE Internship Program</strong> submission</p>"
    "</div>",
    unsafe_allow_html=True
)

