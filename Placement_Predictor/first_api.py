from fastapi import FastAPI
from pydantic import BaseModel
import joblib as jb
import pandas as pd
app = FastAPI()

encoder = jb.load("encoder_new")
scaler = jb.load("scaler_new")
model = jb.load("model_new")
vars = {}

class Vars(BaseModel):
    gender: str
    ssc_p : float
    ssc_b : str
    hsc_p : float
    hsc_b : str
    hsc_s : str
    degree_p: float
    degree_t: str

@app.post("/predict")

def pred_placement(user_inp : Vars):

    data = pd.DataFrame([{
        "gender": user_inp.gender,
        "ssc_p": user_inp.ssc_p,
        "ssc_b": user_inp.ssc_b,
        "hsc_p": user_inp.hsc_p,
        "hsc_b": user_inp.hsc_b,
        "hsc_s": user_inp.hsc_s,
        "degree_p": user_inp.degree_p,
        "degree_t": user_inp.degree_t
    }])

    data = encoder.transform(data)
    data = scaler.transform(data)
    user_inp_predictn = model.predict(data)

    if user_inp_predictn[0]:
        return {"result":"Likely to be Placed !"}
    else:
        return {"result":"Not likely to be Placed :("}
