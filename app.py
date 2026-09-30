import streamlit as st
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("🩺 Early Diabetes Risk Prediction")

st.markdown(
    "### AI-powered diabetes risk estimation using Random Forest"
)

st.write(
    "Enter the patient's health information below to estimate "
    "the likelihood of diabetes."
)
st.sidebar.title("About the Project")

st.sidebar.write(
    """
    This project uses a Random Forest machine learning model
    trained on the Pima Indians Diabetes dataset.
    
    The model uses 8 health-related features to estimate
    diabetes risk.
    """
)

st.sidebar.warning(
    "This application is for educational purposes only "
    "and should not be used as a medical diagnosis."
)

st.markdown(
    "Enter your health information below to estimate diabetes risk."
)

st.info(
    "This tool is for educational purposes only and is not a medical diagnosis."
)
# Input fields
# Create two columns
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=1
    )

    glucose = st.number_input(
        "Glucose",
        min_value=0,
        max_value=300,
        value=120
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=200,
        value=70
    )

    skin_thickness = st.number_input(
        "Skin Thickness",
        min_value=0,
        max_value=100,
        value=20
    )

with col2:
    insulin = st.number_input(
        "Insulin",
        min_value=0,
        max_value=900,
        value=80
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0
    )

    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )
# Prediction button
if st.button("Predict Diabetes Risk"):

    input_data = [[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]]

    # Prediction
    prediction = model.predict(input_data)

    # Probability
    probability = model.predict_proba(input_data)

    risk_probability = probability[0][1] * 100

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("🔴 Higher diabetes risk predicted")
        st.write(
            "The model estimates a higher likelihood of diabetes based on the entered values."
        )
    else:
        st.success("🟢 Lower diabetes risk predicted")
        st.write(
            "The model estimates a lower likelihood of diabetes based on the entered values."
        )
st.metric(
    label="Diabetes Risk Probability",
    value=f"{risk_probability:.2f}%"
)

st.progress(int(risk_probability))
st.divider()

st.subheader("🧠 How It Works")

st.write("""
1. The user enters 8 health-related parameters.
2. The inputs are passed to the trained Random Forest model.
3. The model analyzes the input patterns learned from the diabetes dataset.
4. It predicts the diabetes risk as 0 or 1.
5. The application also displays the estimated probability of diabetes risk.
""")
