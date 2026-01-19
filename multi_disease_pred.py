import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

try:
    # Load the saved models
    diabetes_model = pickle.load(open('ml models/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('ml models/heart_disease_model.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons=['activity', 'heart'],
                           default_index=0)
    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    # Input fields for diabetes prediction
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
    glucose = st.number_input('Glucose Level', min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input('Blood Pressure Value', min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input('Skin Thickness Value', min_value=0, max_value=100, value=20)
    insulin = st.number_input('Insulin Level', min_value=0, max_value=900, value=79)
    bmi = st.number_input('BMI Value', min_value=0.0, max_value=70.0, value=25.0)
    dpf = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, max_value=2.5, value=0.5)
    age = st.number_input('Age of the Person', min_value=1, max_value=120, value=30)
    
    # Prediction button
    if st.button('Predict Diabetes'):
        input_data = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age)
        input_data_reshaped = [input_data]
        
        # Make prediction
        prediction = diabetes_model.predict(input_data_reshaped)
        
        if prediction[0] == 1:
            st.error('The person is likely to have Diabetes.')
        else:
            st.success('The person is unlikely to have Diabetes.')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    # Input fields for heart disease prediction
    age = st.number_input('Age', min_value=1, max_value=120, value=50)
    sex = st.number_input('Sex (0=Female, 1=Male)', min_value=0, max_value=1, value=1)
    cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, value=0)
    trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=200, value=120)
    chol = st.number_input('Cholesterol', min_value=0, max_value=400, value=200)
    fbs = st.number_input('Fasting Blood Sugar (0=No, 1=Yes)', min_value=0, max_value=1, value=0)
    restecg = st.number_input('Resting ECG (0-2)', min_value=0, max_value=2, value=0)
    thalach = st.number_input('Max Heart Rate', min_value=0, max_value=250, value=150)
    exang = st.number_input('Exercise Induced Angina (0=No, 1=Yes)', min_value=0, max_value=1, value=0)
    oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=10.0, value=1.0)
    slope = st.number_input('ST Slope (0-2)', min_value=0, max_value=2, value=1)
    ca = st.number_input('Coronary Artery Calcification (0-4)', min_value=0, max_value=4, value=0)
    thal = st.number_input('Thalassemia (0-3)', min_value=0, max_value=3, value=2)
    
    if st.button('Predict Heart Disease'):
        input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        input_data_reshaped = [input_data]
        
        prediction = heart_disease_model.predict(input_data_reshaped)
        
        if prediction[0] == 1:
            st.error('The person is likely to have Heart Disease.')
        else:
            st.success('The person is unlikely to have Heart Disease.')