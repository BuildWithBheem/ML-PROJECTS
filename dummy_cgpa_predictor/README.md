# 🎓 CGPA Prediction System

A Machine Learning project that predicts a student's CGPA using academic habits and lifestyle factors.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Polynomial Regression
- FastAPI
- Streamlit
- Joblib

## Model Performance

| Model | R² Score |
|---------|---------|
| Polynomial Regression (Degree 2) | 0.93 |
| Random Forest Regressor | 0.85 |
| Decision Tree Regressor | 0.85 |

Polynomial Regression achieved the highest performance and was selected for deployment.

## Features

- CGPA Prediction
- FastAPI Backend
- Streamlit Frontend
- Interactive User Interface
- Real-time Predictions


## Start the FastAPI Backend

- uvicorn app:app --reload

## Start the Streamlit Frontend

- streamlit run cgpa_frontend.py