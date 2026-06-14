import streamlit as st
import numpy as np
import pickle
def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
        }

        h1 {
            color: #00c6ff;
        }

        .stButton>button {
            background-color: #00c6ff;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
        }

        .stButton>button:hover {
            background-color: #0072ff;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺", layout="wide")
import streamlit as st

st.set_page_config(layout="wide")

# Make all labels white
st.markdown("""
<style>
    label, .st-emotion-cache-16txtl3, .st-emotion-cache-1wivap2 {
        color: white !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }
    .st-emotion-cache-10trblm {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
# Image sizing CSS
st.markdown("""
<style>
img {
    width: 100% !important;
    height: 250px !important;
    object-fit: cover !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)
# load model
model = pickle.load(open('model.pkl','rb'))
# Title and subtitle
st.markdown("<h1 style='text-align: center;'>💙 Diabetes Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Smart health risk analysis powered by Machine Learning</p>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image("image.png",use_container_width=True)

with col2:
    st.image("image1.png",use_container_width=True)
st.write("")
st.write("")
st.markdown("""
<div style='background-color:#1e2a38;padding:20px;border-radius:15px'>
<h3 style='color:white;'>🧠 About This App</h3>
<p style='color:white;'>
This application predicts the likelihood of diabetes using Machine Learning.
Enter patient details below to get instant prediction.
</p>
</div>
""", unsafe_allow_html=True)
st.write("")
st.markdown("<p style='color:white;'>Enter Patient Details</p>", unsafe_allow_html=True)
# Input fields
# Create 2 columns
st.markdown("<p style='color:white;'>Please enter accurate medical details for better prediction</p>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("🤰 Pregnancies (count)", min_value=0, max_value=20, step=1)
    glucose = st.number_input("🩸 Glucose Level (mg/dL)", min_value=0, max_value=300, step=1)
    bp = st.number_input("💓 Blood Pressure (mm Hg)", min_value=0, max_value=200, step=1)
    skin = st.number_input("📏 Skin Thickness (mm)", min_value=0, max_value=100, step=1)

with col2:
    insulin = st.number_input("💉 Insulin Level (μU/mL)", min_value=0, max_value=900, step=1)
    bmi = st.number_input("⚖️ BMI (kg/m²)", min_value=0.0, max_value=70.0, step=0.1, format="%.1f")
    dpf = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0, max_value=3.0, step=0.001, format="%.3f")
    age = st.number_input("🎂 Age (years)", min_value=1, max_value=120, step=1)
st.markdown("---")
# Prediction button
import time
st.write("")
if st.button("🔍 Predict"):
     with st.spinner("Analyzing..."):
        time.sleep(1)
        input_data = np.array([[pregnancies,glucose,bp,skin,insulin,bmi,dpf,age]])
        prediction = model.predict(input_data)
        if prediction[0] == 1 :
           st.error("⚠️ High Risk of Diabetes")
        else :
           st.success("✅ Low Risk of Diabetes")
# Footer
st.write("")
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built by Sangeeta Dhankhar 🚀</p>", unsafe_allow_html=True)
