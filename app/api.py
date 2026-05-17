from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("models/xgb_credit_model.pkl")
scaler = joblib.load("models/scaler.pkl")


@app.get("/")
def home():
    return {"message": "Credit Risk Model"}


@app.post("/predict")
def predict(data: dict):
    try:
    
        features = np.array(list(data.values())).reshape(1, -1)

        features_scaled = scaler.transform(features)

        prob = model.predict_proba(features_scaled)[0][1]

        if prob < 0.3:
            risk = "Low Risk"
        elif prob < 0.7:
            risk = "Medium Risk"
        else:
            risk = "High Risk"

        return {
            "default_probability": float(prob),
            "risk_level": risk
        }

    except Exception as e:
        return {"error": str(e)}