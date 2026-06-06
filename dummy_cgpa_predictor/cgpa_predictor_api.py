from fastapi import FastAPI
from pydantic import BaseModel
import joblib as jb
import pandas as pd
app = FastAPI()
poly_features = jb.load("poly_features")
poly_reg_model  = jb.load("Poly_reg_model")
class CGPA_inputs(BaseModel):
    study_hours_per_week: float
    attendance_pct: float
    assignments_submitted_pct: float
    sleep_hours_per_day: float
    coding_practice_hrs_per_week: float
    backlogs_prev_semesters: int
    social_media_usage_hrs_per_day: float
    semester_number: int

@app.post("/cgpa-predict")

def cg_prediction(user_inp : CGPA_inputs):
    data = pd.DataFrame([{
    "study_hours_per_week": user_inp.study_hours_per_week,
    "attendance_pct": user_inp.attendance_pct,
    "assignments_submitted_pct": user_inp.assignments_submitted_pct,
    "sleep_hours_per_day": user_inp.sleep_hours_per_day,
    "coding_practice_hrs_per_week": user_inp.coding_practice_hrs_per_week,
    "backlogs_prev_semesters": user_inp.backlogs_prev_semesters,
    "social_media_usage_hrs_per_day": user_inp.social_media_usage_hrs_per_day,
    "semester_number": user_inp.semester_number
    }])
    data = poly_features.transform(data)
    predict = poly_reg_model.predict(data)
    if float(predict[0]) > 10:
        return {"CGPA Predicted": 10}
    return {"CGPA Predicted":float(predict[0])}