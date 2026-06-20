import streamlit as st
import joblib

st.set_page_config(page_title="HerPulse", page_icon="💜")

st.title("💜 HerPulse")
st.subheader("PCOS Prediction System")

model = joblib.load("herpulse_lite_model.pkl")

age = st.number_input("Age")
bmi = st.number_input("BMI")
cycle_length = st.number_input("Cycle Length (days)")

weight_gain = st.selectbox("Weight Gain", ["No", "Yes"])
hair_growth = st.selectbox("Hair Growth", ["No", "Yes"])
skin_darkening = st.selectbox("Skin Darkening", ["No", "Yes"])

weight_gain = 1 if weight_gain == "Yes" else 0
hair_growth = 1 if hair_growth == "Yes" else 0
skin_darkening = 1 if skin_darkening == "Yes" else 0

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

    probability = model.predict_proba(input_data)

    risk_percentage = probability[0][1] * 100

    st.subheader("💜 Prediction Result")

    st.write(f"PCOS Risk: {risk_percentage:.2f}%")

    if risk_percentage <= 30:
        st.success("🟢 Low Risk")

    elif risk_percentage <= 70:
        st.warning("🟡 Moderate Risk")

    else:
        st.error("🔴 High Risk")

    if prediction[0] == 1:
        st.error("⚠️ PCOS Detected")
    else:
        st.success("✅ PCOS Not Detected")

st.markdown("---")

st.caption(
    "⚠️ This prediction is based on machine learning and is intended for educational purposes only. Please consult a healthcare professional for medical diagnosis and treatment."
)

st.sidebar.title("💜 HerPulse")

st.sidebar.info("""
PCOS Prediction System

Model: Random Forest

Accuracy: 88.07%

Built with:
• Python
• Scikit-learn
• Streamlit
""")