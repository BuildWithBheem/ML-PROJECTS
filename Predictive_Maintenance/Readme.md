# 🔧 AI-Powered Predictive Maintenance System using ANN & FastAPI

An end-to-end Machine Learning project that predicts industrial machine failures using an Artificial Neural Network (ANN). The trained model is deployed through a FastAPI REST API, allowing real-time failure prediction from machine sensor inputs.

---

## 🚀 Features

* Artificial Neural Network built using TensorFlow/Keras
* Handles imbalanced datasets using SMOTE
* Feature preprocessing using:

  * ColumnTransformer
  * OneHotEncoder
  * StandardScaler
* FastAPI deployment
* REST API for real-time predictions
* Returns failure prediction along with confidence probability

---

## 📊 Dataset

**AI4I 2020 Predictive Maintenance Dataset**

Features used:

* Machine Type (L, M, H)
* Air Temperature (K)
* Process Temperature (K)
* Rotational Speed (RPM)
* Torque (Nm)

Target:

* Machine Failure (0 = No Failure, 1 = Failure)

---

## 🧠 Machine Learning Pipeline

```text
Raw Data
    │
    ▼
Data Cleaning
    │
    ▼
One-Hot Encoding (Machine Type)
    │
    ▼
Train-Test Split
    │
    ▼
Standard Scaling
    │
    ▼
SMOTE (Training Set Only)
    │
    ▼
Artificial Neural Network
    │
    ▼
Model Evaluation
    │
    ▼
FastAPI Deployment
```

---

## 🏗️ Model Architecture

```text
Input Layer
      │
      ▼
Dense (64) + ReLU
      │
      ▼
Dense (32) + ReLU
      │
      ▼
Dense (16) + ReLU
      │
      ▼
Dense (8) + ReLU
      │
      ▼
Dense (1) + Sigmoid
```

Loss Function:

* Binary Crossentropy

Optimizer:

* Adam

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* FastAPI
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Uvicorn
* Imbalanced-Learn (SMOTE)

---

## 📁 Project Structure

```
Predictive_Maintenance/
│
├── Neural_Network.h5
├── Feature_Scaling.pkl
├── ColumnTransformer.pkl
├── pm.py
├── requirements.txt
├── README.md
└── ai4i2020.csv
```

---

## ▶️ Running the API

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI

```bash
uvicorn pm:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📤 API Request

```json
{
    "Type": "L",
    "Air_tp": 298.2,
    "Process_tp": 308.7,
    "Rot_sp": 1500,
    "Trq": 40
}
```

---

## 📥 API Response

```json
{
    "Prediction": "No Failure Predicted",
    "Failure_Probability": 0.0003
}
```

---

## 📈 Model Improvements

To improve failure detection in this highly imbalanced dataset:

* Applied **SMOTE** on the training data.
* Compared baseline ANN against SMOTE-balanced training.
* Tuned the classification threshold to improve recall for the failure class.
* Evaluated the trade-off between false positives and missed failures using confusion matrices and classification reports.

---

## 🔮 Future Improvements

* Streamlit dashboard
* ESP32 integration for live IoT sensor data
* SHAP model explainability
* Docker containerization
* Cloud deployment
* Real-time monitoring dashboard

---

## 👨‍💻 Author

**Bhimaraju Sai Koundinya**

B.Tech Computer Science (AI & ML)

KIIT University

