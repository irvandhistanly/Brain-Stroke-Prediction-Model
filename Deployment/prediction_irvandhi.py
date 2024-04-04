import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model_svm_tuned.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Function to run the Streamlit app
def run():
    # Set page title and sidebar image
    st.write('BRAIN STROKE PREDICTOR')

    # Introduction
    st.subheader("📊 Prediction of Brain Stroke")
    st.write("Welcome to the Brain Stroke Predictor app! This app predicts whether a patient is likely to have a brain stroke based on provided information.")

    # Input form
    st.markdown('## 📝 Input Data')
    with st.form('my_form'):
        # Input fields
        gender = st.selectbox('🚻 Gender', options=['Male', 'Female'])
        age = st.number_input('🧒🏻 Age', min_value=1, max_value=110)
        st.markdown("**Hypertension:** 0 if the patient doesn't have any hypertension, 1 if the patient has a hypertension")
        hypertension = st.selectbox('💉 Hypertension', options=[0, 1])
        st.markdown("**Heart diseases:** 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart diseases")
        heart_disease = st.selectbox('❤️ Heart Disease', options=[0, 1])
        ever_married = st.selectbox('💍 Ever Married', options=['Yes', 'No'])
        work_type = st.selectbox('👩‍💼 Work Type', options=['Private', 'Self-employed', 'Govt_job', 'Children'])
        residence_type = st.selectbox('🏠 Residence Type', options=['Urban', 'Rural'])
        avg_glucose_level = st.number_input('🍬 Average Glucose Level', min_value=0.0, max_value=500.0)
        bmi = st.number_input('🧍 BMI', min_value=10.0, max_value=100.0)
        smoking_status = st.selectbox('🚬 Smoking Status', options=['formerly smoked', 'never smoked', 'smokes'])

        submitted = st.form_submit_button('🔍 Let\'s Check!')

    # Create DataFrame from user input
    data = {
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'ever_married': ever_married,
        'work_type': work_type,
        'residence_type': residence_type,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'smoking_status': smoking_status
    }

    df = pd.DataFrame([data])
    st.dataframe(df)

    # Make prediction
    if submitted:
        prediction = model.predict(df)

        # Display prediction result
        if prediction[0] == 0:
            st.write('🟢 No Stroke')
        else:
            st.write('🔴 Stroke')

if __name__== '__main__':
    run()
