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
