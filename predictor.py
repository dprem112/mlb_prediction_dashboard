import joblib
import numpy as np

# Load model and scaler
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_game(features):
    X = scaler.transform([features])
    prediction = model.predict(X)[0]
    confidence = model.predict_proba(X)[0][prediction]
    return prediction, confidence
