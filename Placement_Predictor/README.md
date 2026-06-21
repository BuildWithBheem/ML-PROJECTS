# Placement Prediction System

A Machine Learning web application that predicts whether a student is likely to be placed based on academic performance and educational background.

## Overview

This project uses a trained Machine Learning model to analyze student academic details and predict placement outcomes. The model is deployed using FastAPI as the backend API and Streamlit as the frontend interface.

## Features

- Student placement prediction
- FastAPI REST API
- Streamlit web interface
- Data preprocessing using encoding and scaling
- Trained Scikit-Learn model
- Real-time predictions

## Tech Stack

- Python
- Scikit-Learn
- Pandas
- NumPy
- FastAPI
- Streamlit
- Joblib

## Project Structure

```text
dummy_placement_predictor/
│
├── first.py
├── first_api.py
├── model_new
├── scaler_new
├── encoder_new
├── requirements.txt
├── placement_prediction.ipynb
└── README.md
```

## Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
FastAPI Backend
 │
 ▼
Preprocessing Pipeline
 │
 ├── Encoding
 │
 └── Scaling
 │
 ▼
Trained ML Model
 │
 ▼
Prediction
 │
 ▼
User
```

## Running the FastAPI Server

```bash
uvicorn api:app --reload
```

## Running the Streamlit Application

```bash
streamlit run app.py
```

## Sample Prediction Inputs

- Gender
- SSC Percentage
- SSC Board
- HSC Percentage
- HSC Board
- HSC Stream
- Degree Percentage
- Degree Type

## Author

Bhimaraju Sai Koundinya
B.Tech CSE AI/ML, KIIT University