import streamlit as st
import requests
import time as t
st.title("CGPA Predictor")
st.write("# Predict your next CGPA from your habits")

col1,col2 = st.columns([1,2])

with col1:
    study = st.number_input(
    "Study Hours Per Week",
    min_value=0.0,
    max_value=50.0,
    step=0.5,
    value=20.0
    )
    att = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    value=75.0
    )

    asg_sub = st.number_input(
    "Assignments Submitted Percentage",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    value=80.0
    )

    sleep_hrs = st.number_input(
    "Sleep Hours Per Day",
    min_value=0.0,
    max_value=24.0,
    step=0.5,
    value=7.0
    )

    coding= st.number_input(
    "Coding Practice Hours Per Week",
    min_value=0.0,
    max_value=50.0,
    step=0.5,
    value=10.0
    )

    backlogs = st.number_input(
    "Previous Semester Backlogs",
    min_value=0,
    max_value=20,
    step=1,
    value=0
    )

    social_usage = st.number_input(
    "Social Media Usage Hours Per Day",
    min_value=0.0,
    max_value=24.0,
    step=0.5,
    value=3.0
    )

    sem_no = st.number_input(
    "Semester Number",
    min_value=1,
    max_value=8,
    step=1,
    value=4
    )

if st.button("Predict CGPA"):
    data = {
    "study_hours_per_week": study,
    "attendance_pct": att,
    "assignments_submitted_pct": asg_sub,
    "sleep_hours_per_day": sleep_hrs,
    "coding_practice_hrs_per_week": coding,
    "backlogs_prev_semesters": backlogs,
    "social_media_usage_hrs_per_day": social_usage,
    "semester_number": sem_no
    }
    response = requests.post(
    "http://127.0.0.1:8000/cgpa-predict",
    json = data)
    prediction = response.json()["CGPA Predicted"]
    with st.spinner("Loading, please wait.."):
        t.sleep(3.5)
        st.success(f"{prediction:.2f}")



