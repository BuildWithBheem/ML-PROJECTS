from fastapi import FastAPI
from pydantic import BaseModel
import joblib as jb
import pandas as pd
import tensorflow as tf
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
app = FastAPI()
ann = tf.keras.models.load_model("Neural_Network.h5")
sc = jb.load("Feature_Scaling.pkl")
ct = jb.load("OneHotEncoder_new.pkl")
class sense(BaseModel):
    Type : str
    Air_tp : float
    Process_tp: float
    Rot_sp: int
    Trq: float


@app.post("/maintain")
def Machine(user_inp: sense):
    data = pd.DataFrame(
        {
            "Type": [user_inp.Type],
            "Air temperature [K]":[user_inp.Air_tp],
            "Process temperature [K]":[user_inp.Process_tp],
            "Rotational speed [rpm]":[user_inp.Rot_sp],
            "Torque [Nm]":[user_inp.Trq]
        }
    )
    data = ct.transform(data)
    data = sc.transform(data)
    prob = ann.predict(data)
    predictn = (prob[0][0] > 0.3)
    if predictn == 1:
        predictn = 'Machine about to fail'
    if predictn == 0:
        predictn = 'All Good'
    return {"Machine_Failure": predictn, "Probaility": float(prob[0][0]) }