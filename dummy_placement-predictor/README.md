\# Placement Prediction System



A Machine Learning web application that predicts whether a student is likely to be placed based on academic performance and educational background.



\## Overview



This project uses a trained Machine Learning model to analyze student academic details and predict placement outcomes. The model is deployed using FastAPI as the backend API and Streamlit as the frontend interface.



\## Features



\- Student placement prediction

\- FastAPI REST API

\- Streamlit web interface

\- Data preprocessing using encoding and scaling

\- Trained Scikit-Learn model

\- Real-time predictions



\## Tech Stack



\- Python

\- Scikit-Learn

\- Pandas

\- NumPy

\- FastAPI

\- Streamlit

\- Joblib



\## Project Structure



```text

dummy\_placement\_predictor/

│

├── first.py

├── first\_api.py

├── model\_new

├── scaler\_new

├── encoder\_new

├── requirements.txt

├── placement\_prediction.ipynb

└── README.md

```



\## Architecture



```text

User

&#x20;│

&#x20;▼

Streamlit UI

&#x20;│

&#x20;▼

FastAPI Backend

&#x20;│

&#x20;▼

Preprocessing Pipeline

&#x20;│

&#x20;├── Encoding

&#x20;│

&#x20;└── Scaling

&#x20;│

&#x20;▼

Trained ML Model

&#x20;│

&#x20;▼

Prediction

&#x20;│

&#x20;▼

User

```



\## Running the FastAPI Server



```bash

uvicorn api:app --reload

```



\## Running the Streamlit Application



```bash

streamlit run app.py

```



\## Sample Prediction Inputs



\- Gender

\- Class 10 Percentage

\- Class 10 Board

\- Class 12 Percentage

\- Class 12 Board

\- Class 12 Stream

\- Degree Percentage

\- Degree Type



\## Author



Bhimaraju Sai Koundinya

B.Tech CSE AI/ML, KIIT University

