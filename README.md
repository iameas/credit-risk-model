# Credit Risk Prediction System (End-to-End Machine Learning Project)

An end-to-end, production-style machine learning system that predicts loan default risk and explains decisions using interpretable AI (SHAP). This project simulates a real-world credit scoring pipeline used in fintech and banking systems:
from raw data → model training → API deployment → interactive user interface → explainable AI layer.

---

# Table of Contents

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

# Project Overview

This system predicts whether a loan applicant is likely to default based on historical financial behavior and credit data.

Unlike basic ML notebooks, this project is fully deployed with:

- A trained machine learning model
- A REST API for real-time predictions
- A web-based UI dashboard
- Explainable AI to interpret predictions

The goal is not just prediction, but **decision transparency**.

---

# Problem Statement

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

# Objectives

- Predict loan default probability
- Classify applicants into risk categories
- Provide interpretable explanations for predictions
- Build an end-to-end deployable ML system

---

# System Architecture
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

# Dataset Information

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

# Machine Learning Pipeline

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

# Model Explainability (SHAP)

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

# Tech Stack

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

# Project Structure

```

credit-risk-model/
│
├── data/
│   └── cs-training.csv
│
├── models/
│   └── model_package.pkl
│
├── src/
│   └── train.py
│
├── app/
│   ├── api.py
│   └── streamlit\_app.py
│
├── requirements.txt
└── README.md

---

# Installation Guide
```
git clone <repo-url>
cd credit-risk-model
```
