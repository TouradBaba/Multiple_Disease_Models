import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


# Load the models
heart_disease_model = pickle.load(open('Saved Models/heart_disease_model.sav', 'rb'))
parkinson_model = pickle.load(open('Saved Models/parkinsons_model.sav', 'rb'))
diabetes_model = pickle.load(open('Saved Models/diabetes_model.sav', 'rb'))


def heart_pred(data):
    prediction = heart_disease_model.predict([data])
    if prediction == 0:
        return 'Normal'
    else:
        return 'You have a Heart Disease'


def diab_predict(data):
    prediction = diabetes_model.predict([data])
    if prediction == 0:
        return 'Normal'
    else:
        return 'Diabetic'


# Creating a sidebar
with st.sidebar:
    st.title("Multiple ML Models for Predictions of Heart Diseases, Diabetes and Parkinson's diseases")
    st.subheader('Select a Model')
    model_selection = option_menu(
        'Models',
        ['Heart Disease Model', "Parkinson's Model", 'Diabetes Model'],icons=['heart-pulse-fill','activity','hospital-fill'] , default_index=0)



try:
    if model_selection == 'Heart Disease Model':
        st.title('The heart diseases model page')
        st.subheader('Enter the data needed to predict whether you have a heart disease or not')
        # Getting data from the user
        # Number of columns
        col1,col2,col3 = st.columns(3)
        with col1:
            age = st.text_input('Age')
        with col2:
            sex = st.text_input('Sex')
        with col3:
            cp = st.text_input('CP value')
        with col1:
            trestbps = st.text_input('Trestbps value')
        with col2:
            chol = st.text_input('CHOL value')
        with col3:
            fbs = st.text_input('FBS value')
        with col1:
            restecg = st.text_input('REST ECG value')
        with col2:
            thalach = st.text_input('THALACH value')
        with col3:
            exang = st.text_input('EXANG value')
        with col1:
            oldpeak = st.text_input('Old Peak value')
        with col2:
            slope = st.text_input('Slope value')
        with col3:
            ca = st.text_input('CA value')
        with col1:
            thal = st.text_input('THAL value')
        # Prediction
        prediction_result = ''
        # Button
        if st.button('Predict'):
            prediction_result = heart_pred(
                (float(age),float(sex),float(cp),float(trestbps),float(chol),float(fbs),float(restecg) ,float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)))
        st.success(prediction_result)
except Exception as e:
    # Print the exception details for debugging
    print(f"An exception occurred: {e}")
    # Return an appropriate message
    st.warning('An error occurred. Please check your input data.')

try:
    if model_selection == "Parkinson's Model":
        st.title("The Parkinson's disease model page")
        st.subheader("Enter the data needed to predict whether you have Parkinson's disease or not")
        # Getting data from the user
        MDVP_Fo_in_Hz = st.text_input(' MDVP:Fo(Hz)')
        MDVP_Fhi_in_Hz = st.text_input('MDVP:Fhi(Hz)')
        MDVP_Flo_in_Hz = st.text_input('MDVP:Flo(Hz)')
        MDVP_Jitter_in_percent = st.text_input("MDVP:Jitter (%)")
        MDVP_Jitter_in_Abs = st.text_input("MDVP Jitter (Abs)")
        MDVP_RAP = st.text_input("MDVP RAP")
        MDVP_PPQ = st.text_input("MDVP PPQ")
        Jitter_DDP = st.text_input("Jitter DDP")
        MDVP_Shimmer = st.text_input("MDVP Shimmer")
        MDVP_Shimmer_in_dB = st.text_input("MDVP Shimmer(dB)")
        Shimmer_APQ3 = st.text_input("Shimmer APQ3")
        Shimmer_APQ5 = st.text_input("Shimmer APQ5")
        MDVP_APQ = st.text_input("MDVP APQ")
        Shimmer_DDA = st.text_input("Shimmer DDA")
        NHR = st.text_input("NHR")
        HNR = st.text_input('HNR')
        RPDE = st.text_input('RPDE')
        DFA = st.text_input('DFA')
        spread1 = st.text_input('Spread 1')
        spread2 = st.text_input('Spread 2')
        D2 = st.text_input('D2')
        PPE = st.text_input('PPE')

        prediction_result = ''
        # Button
        if st.button('Predict'):
            # Reshape input data as a 2D array with a single sample
            input_data = np.array(
                [MDVP_Fo_in_Hz, MDVP_Fhi_in_Hz, MDVP_Flo_in_Hz, MDVP_Jitter_in_percent, MDVP_Jitter_in_Abs, MDVP_RAP,
                 MDVP_PPQ,
                 Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_in_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR,
                 HNR, RPDE, DFA,
                 spread1, spread2, D2, PPE]).reshape(1, -1)
            prediction_result = parkinson_model.predict(input_data)
            if prediction_result == 0:
                prediction_result = 'Normal'
            else:
                prediction_result = "You have Parkinson's disease"
            st.success(prediction_result)
except Exception as e:
    # Print the exception details for debugging
    print(f"An exception occurred: {e}")
    # Return an appropriate message
    st.warning('An error occurred. Please check your input data.')

try:
    if model_selection == 'Diabetes Model':
        st.title('The diabetes prediction page')
        st.subheader('Enter the data needed to predict whether you have diabetes or not')
        # Getting data from the user
        pregnancies = st.text_input('Number of pregnancies')
        glucose = st.text_input('Glucose level')
        bloodpressure = st.text_input('Blood Pressure value')
        skinthickness = st.text_input('Skin thickness value')
        insulin = st.text_input('Insulin level')
        bmi = st.text_input('BMI value')
        diabetespedigreefunction = st.text_input('Diabetes Pedigree Function value')
        age = st.text_input('Age')

        # Prediction
        prediction_result = ''
        # Button
        if st.button('Predict'):
            prediction_result = diab_predict(
                (pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age))
        st.success(prediction_result)

except Exception as e:
    # Print the exception details for debugging
    print(f"An exception occurred: {e}")
    # Return an appropriate message
    st.warning('An error occurred. Please check your input data.')