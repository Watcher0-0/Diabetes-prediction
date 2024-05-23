import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Diabetes Prediction",
    layout="wide",
    page_icon="⚕"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        color: black;
    }
    .stTextInput>div>div>input {
        background-color: #fff;
        color: black;
    }
    .stNumberInput>div>div>input {
        background-color: #fff;
        color: black;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .title {
        color: blue;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the saved models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))

# Title with custom color
st.markdown('<h1 class="title">Diabetes Prediction using SVM</h1>', unsafe_allow_html=True)

# Input fields
with st.form(key='diabetes_form'):
    st.subheader("Patient Details")

    col1, col2 = st.columns(2)

    with col1:
        pre = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
        bp = st.number_input('Blood Pressure Value', min_value=0, max_value=200, step=1)
        iv = st.number_input('Insulin Level', min_value=0, max_value=900, step=1)
        ped = st.number_input('Diabetes Pedigree Function value', min_value=0.0, max_value=2.5, step=0.01)

    with col2:
        glu = st.number_input('Glucose Level', min_value=0, max_value=200, step=1)
        stv = st.number_input('Skin Thickness value', min_value=0, max_value=100, step=1)
        bmi = st.number_input('BMI value', min_value=0.0, max_value=70.0, step=0.1)
        age = st.number_input('Age of the Person', min_value=0, max_value=120, step=1)

    submit_button = st.form_submit_button(label='Get Diabetes Test Result')

# Prediction and result display
if submit_button:
    try:
        user_input = [pre, glu, bp, stv, iv, bmi, ped, age]
        diabetes_prediction = diabetes_model.predict([user_input])

        if diabetes_prediction[0] == 1:
            st.success('The person does **not** have diabetes.')
        else:
            st.error('The person **has** diabetes.')

    except Exception as e:
        st.error(f"An error occurred: {e}")
