import streamlit as st
import joblib

st.set_page_config(page_title="HerPulse", page_icon="💜")

st.title("💜 HerPulse")
st.subheader("PCOS Prediction System")

model = joblib.load("herpulse_lite_model.pkl")

st.success("Model loaded successfully!")

age = st.number_input("Age")
bmi = st.number_input("BMI")
cycle_length = st.number_input("Cycle Length (days)")

weight_gain = st.selectbox("Weight Gain", [0, 1])
hair_growth = st.selectbox("Hair Growth", [0, 1])
skin_darkening = st.selectbox("Skin Darkening", [0, 1])

amh = st.number_input("AMH (ng/mL)")
follicle_l = st.number_input("Follicle No. (L)")
follicle_r = st.number_input("Follicle No. (R)")

if st.button("Predict"):

    input_data = [[
        age,
        bmi,
        cycle_length,
        weight_gain,
        hair_growth,
        skin_darkening,
        amh,
        follicle_l,
        follicle_r
    ]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ PCOS Detected")
    else:
        st.success("✅ PCOS Not Detected")