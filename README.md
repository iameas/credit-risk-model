# Credit Risk Prediction System (End-to-End Machine Learning Project)

An end-to-end, production-style machine learning system that predicts loan default risk and explains decisions using interpretable AI (SHAP). This project simulates a real-world credit scoring pipeline used in fintech and banking systems:
from raw data → model training → API deployment → interactive user interface → explainable AI layer.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [System Architecture](#system-architecture)
- [Dataset Information](#dataset-information)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Model Explainability (SHAP)](#model-explainability-shap)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [How to Run the Project](#how-to-run-the-project)
- [API Documentation](#api-documentation)
- [Frontend (Streamlit UI)](#frontend-streamlit-ui)
- [Example Prediction](#example-prediction)
- [Key Features](#key-features)
- [Challenges Faced](#challenges-faced)
- [Lessons Learned](#lessons-learned)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Project Overview

This system predicts whether a loan applicant is likely to default based on historical financial behavior and credit data.

Unlike basic ML notebooks, this project is fully deployed with:

- A trained machine learning model
- A REST API for real-time predictions
- A web-based UI dashboard
- Explainable AI to interpret predictions

The goal is not just prediction, but **decision transparency**.

---

## Problem Statement

Financial institutions need to evaluate loan applicants quickly and accurately.

However:
- Manual evaluation is slow
- Human bias may exist
- Black-box models are not trustworthy

This project solves that by building a system that is:
- Automated
- Consistent
- Explainable

---

## Objectives

- Predict loan default probability
- Classify applicants into risk categories
- Provide interpretable explanations for predictions
- Build an end-to-end deployable ML system

---

## System Architecture
User Input (Streamlit UI)
↓
FastAPI Backend (/predict, /explain)
↓
ML Pipeline (XGBoost Model)
↓
Prediction + SHAP Explanation
↓
Response to UI
↓
Visualization (Gauge + Feature Importance)


---

## Dataset Information

The dataset contains credit behavior features such as:

- Revolving utilization of unsecured lines
- Age of borrower
- Debt ratio
- Monthly income
- Number of open credit lines
- Past due history (30–59, 60–89, 90+ days)

Target variable:
```
SeriousDlqin2yrs (0 = No default, 1 = Default)
```

---

## Machine Learning Pipeline

### Steps:

1. Data Cleaning
   - Missing value handling
   - Column normalization

2. Feature Processing
   - StandardScaler applied

3. Model Training
   - XGBoost Classifier
   - Class imbalance handled via `scale_pos_weight`

4. Model Packaging
   - Entire pipeline saved using `joblib`

---

## Model Explainability (SHAP)

SHAP (SHapley Additive Explanations) is used to interpret model decisions.

It answers:

> Why was this loan approved or rejected?

It shows feature contributions such as:
- Debt ratio impact
- Late payment history
- Income effect
- Credit utilization impact

This ensures transparency and trust in predictions.

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- SHAP
- Plotly
- Joblib

---

## Installation Guide
```
git clone https://github.com/iameas/credit-risk-model.git
cd credit-risk-model
```

--- 

## Create virtual environment
```python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies
``pip install -r requirements.txt``

---

## How to Run the Project

### Step 1 — Train Model
``python src/train.py``

### Step 2 — Start API
``uvicorn app.api:app --reload``

### Step 3 — Start Streamlit UI
``streamlit run app/streamlit_app.py``

UI runs at:
``http://localhost:8501``

## API Documentation
### Predict Endpoint: POST *``/predict``*

inputs:

```
{
  "RevolvingUtilizationOfUnsecuredLines": 0.5,
  "age": 35,
  "NumberOfTime30_59DaysPastDueNotWorse": 1,
  "NumberOfTime60_89DaysPastDueNotWorse": 0,
  "NumberOfTimes90DaysLate": 0,
  "DebtRatio": 0.3,
  "MonthlyIncome": 5000,
  "NumberOfOpenCreditLinesAndLoans": 5,
  "NumberRealEstateLoansOrLines": 1,
  "NumberOfDependents": 2
}
```

Output:

```
{
  "default_probability": 0.42,
  "risk_level": "Medium Risk"
}
``` 

### Explain Endpoint: POST *``/explain``*

Output:

```
{
  "DebtRatio": 0.32,
  "NumberOfTimes90DaysLate": 0.28,
  "MonthlyIncome": -0.18
}
```

## Frontend (Streamlit UI)

The UI includes:
- Input form for applicant data
- Risk prediction button
- Gauge chart visualization
- SHAP explanation bar chart
- Risk classification badges
  
## Key Features
- End-to-end ML pipeline
- Real-time prediction API
- Explainable AI system
- Interactive dashboard
- Production-style architecture
- Clean feature engineering pipeline

## Challenges Faced
- Feature mismatch between training and API
- Column naming inconsistencies (hyphen vs underscore)
- API validation errors (422 responses)
- Model input-output alignment issues
- Debugging multi-layer system (UI → API → model)

## Lessons Learned
- ML is easy — system integration is hard
- Consistency in features is critical
- APIs must strictly enforce schema validation
- Explainability increases trust in models
- End-to-end systems matter more than model accuracy alone

## Future Improvements
- Docker containerization
- Cloud deployment (AWS / Render)
- Database logging of predictions
- Authentication system
- Model monitoring dashboard
- Batch prediction API

## Author
Built as a full-stack machine learning engineering project focused on production deployment patterns and explainable AI.

## If You Like This Project
*Feel free to star the repository or connect with me on LinkedIn.*
