import streamlit as st
import time as t
import requests
st.title("Placement Predictor")
st.write("## Enter your details and find out if you're going to be placed")
col1, col2 = st.columns([1, 2])
with col1:
    gender = st.selectbox("Select your Gender", ("M", "F"))
    ssc_b = st.selectbox("Select your Secondary School Board", ("Others", "Central"))
    ssc_p = st.number_input("Enter your SSC percentage",min_value = 0,max_value = 100)
    hsc_b = st.selectbox("Select your Class 12 Board",("Central","Others"))
    hsc_s = st.selectbox("Select your Class 12 Stream",("Commerce","Science","Arts"))
    hsc_p = st.number_input("Enter your Class 12 percentage ",min_value = 0,max_value = 100)
    deg_str = st.selectbox("Select your Degree",("Comm&Mgmt","Sci&Tech","Others"))
    deg_p = st.number_input("Enter your Degree percentage",min_value = 0,max_value = 100)

if st.button("Predict"):
    data = {
        "gender": gender,
        "ssc_p": ssc_p,
        "ssc_b": ssc_b,
        "hsc_p": hsc_p,
        "hsc_b": hsc_b,
        "hsc_s": hsc_s,
        "degree_p": deg_p,
        "degree_t": deg_str
    }

    response_api = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data #Converts the data input to json format
    )
    prediction = response_api.json()["result"]

    with st.spinner("Processing, please wait..."):
        t.sleep(2.5)
        st.write(prediction)
