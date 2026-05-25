# Machine Learning Internship

# ML Internship Projects — INCODEVision

A collection of Machine Learning projects completed as part of my ML Internship at INCODEVision, built using Python and FastAPI.

## Projects

### Task 02 — House Price Prediction
- Predicts house prices in Bengaluru using Linear Regression
- Dataset: Bengaluru House Price Data (Kaggle)
- Model Metrics: R² = 0.65, RMSE = ₹65 Lakhs
- Endpoint: `POST /predict/house-price`

### Task 03 — Spam Email Classifier (In Progress)
- Classifies emails as spam or not spam using NLP
- Endpoint: `POST /predict/spam`

### Task 04 — Customer Churn Prediction (In Progress)
- Predicts customer churn using classification models
- Endpoint: `POST /predict/churn`

## Tech Stack
- Python
- FastAPI
- scikit-learn
- pandas, NumPy
- Jupyter Notebooks
- PyCharm

## Project Structure
ml-internship/
├── app/
│   ├── routes/         # FastAPI route handlers
│   ├── ml/             # Model loading and prediction logic
│   └── utils/
├── datasets/           # Raw datasets
├── notebooks/          # Training notebooks
├── trained_models/     # Saved .pkl models (not tracked in Git)
├── main.py
├── requirements.txt
└── README.md

## Setup
pip install -r requirements.txt

## Run the API
uvicorn main:app --reload

## Author
Sravani — Backend Engineer
