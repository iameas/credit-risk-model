from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import shap
import numpy as np

app = FastAPI()

package = joblib.load("models/model_package.pkl")
model = package["model"]
feature_names = package["features"]
explainer = shap.Explainer(model["model"])

class LoanInput(BaseModel):
    RevolvingUtilizationOfUnsecuredLines: float
    age: int
    NumberOfTime30_59DaysPastDueNotWorse: int
    NumberOfTime60_89DaysPastDueNotWorse: int
    NumberOfTimes90DaysLate: int
    DebtRatio: float
    MonthlyIncome: float
    NumberOfOpenCreditLinesAndLoans: int
    NumberRealEstateLoansOrLines: int
    NumberOfDependents: int

@app.get("/")
def home():
    return {"status": "Credit Risk Predictor API (Running)"}

@app.post("/predict")
def predict(data: LoanInput):

    df = pd.DataFrame([data.dict()])

    df = df.reindex(columns=feature_names, fill_value=0)

    prob = model.predict_proba(df)[0][1]

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

@app.post("/explain")
def explain(data: LoanInput):

    df = pd.DataFrame([data.dict()])
    df = df.reindex(columns=feature_names, fill_value=0)

    shap_values = explainer(df)

    explanation = {
        feature: float(value)
        for feature, value in zip(feature_names, shap_values.values[0])
    }

    sorted_explanation = dict(
        sorted(explanation.items(), key=lambda x: abs(x[1]), reverse=True)
    )

    return {
        "explanation": sorted_explanation
    }