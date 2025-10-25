import streamlit as st
import pandas as pd
import joblib

st.markdown(
    """
<style>
.block-container {
    border: 30px solid #800080;
    outline: 10px solid #0000FF;
    padding: 10px 20px;
    border-radius: 10px;
    }
p   {
    color: purple;
    }
body {
    background-color: rgba(o,30,100,0.3);
    }
h1 {
    color: green;
    font-family: Arial, sans-serif;
    font-size: 25px;
    }
h2 {
    color: green;
    font-family: Arial, sans-serif;
    font-size: 20px;
    }
h3 {
    color: green;
    font-family: Arial, sans-serif;
    font-size:18px;
    }
.stButton>button {
    backgroud-color: rgba(0,0,40,0.2);
    color: brown;
    border: solid;
    padding: 10px 20px;
    cursor: pointer;
}
    </style>
    """,
    unsafe_allow_html=True,
)

model = joblib.load('diabetes_app.pkl')

st.set_page_config(page_title="Diabetes Prediction App",layout= "centered")
st.title("Diabetes Prediction App")
st.write("CAUTION: This application should only be used by a qualified medical practitioner.The developer will not be liable for any wrong use of the application.")
#app title and intro
st.set_page_config(page_title="Micy Diabetes Prediction Application",layout="centered")
st.title("MGN Diabetes Risk Assessment App (Sample model)")
st.write("Fill in the details below to predict the likelihood of diabetes")

#input form
with st.form("Prediction Form"):
    st.subheader("Enter Patient Data")
    col1,col2 = st.columns(2)
    with col1:
        pregnancies= st.slider("Pregnancies",0,10,step=1)
        glucose= st.slider("Glucose",0,200,120)
        blood_pressure= st.slider("BloodPressure",0,140,70)
        bmi= st.number_input("BMI",min_value=0.0,max_value=70.0,value=25.0)
    with col2:
        skin_thickness= st.slider("SkinThickness",0,100,20)
        insulin= st.slider("Insulin",0,900,80)
        diabetes_pedigree= st.number_input("DiabetesPedigreeFunction",0.0,2.5,0.5)
        age= st.selectbox("Age",options= [i for i in range(18,81,1)],index= 2)
    submitted= st.form_submit_button("Predict")
#prediction 
if submitted:
    input_data = pd.DataFrame([[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree,age]],columns= ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Prediction: Likely to be diabetic. Refer the patient for further confirmatory tests.")
    else:
        st.success("Prediction: Negative for diabetes posibility.")

st.write("The table below explains the features used in the application:")
data2= {
    "Feature": ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'],
    "Description":[
        'Number of times pregnant',
        'Plasma glucose concentration',
        'Diastolic blood pressure',
        'Triceps skin fold thickness',
        '2-Hour serum insulin',
        'Body Mass Index(weight/height^2)',
        'Family history of diabetes',
        'Patient age in years',
    ]
}
df2= pd.DataFrame(data2)
st.table(df2)

