import streamlit as st
import requests

import plotly.graph_objects as go


def create_gauge(prob):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={"text": "Default Risk %"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "black"},
            "steps": [
                {"range": [0, 30], "color": "green"},
                {"range": [30, 70], "color": "orange"},
                {"range": [70, 100], "color": "red"},
            ],
        }
    ))
    return fig

st.set_page_config(page_title="Credit Risk Predictor", layout="centered")

st.title("Credit Risk Prediction System")
st.write("Enter applicant details to predict loan default risk.")

RevolvingUtilizationOfUnsecuredLines = st.number_input("Revolving Utilization", 0.0, 10.0, 0.5)
age = st.number_input("Age", 18, 100, 35)

NumberOfTime30_59DaysPastDueNotWorse = st.number_input("30-59 Days Past Due", 0, 20, 1)
NumberOfTime60_89DaysPastDueNotWorse = st.number_input("60-89 Days Past Due", 0, 20, 0)
NumberOfTimes90DaysLate = st.number_input("90+ Days Late", 0, 20, 0)

DebtRatio = st.number_input("Debt Ratio", 0.0, 10.0, 0.3)
MonthlyIncome = st.number_input("Monthly Income", 0.0, 100000.0, 5000.0)

NumberOfOpenCreditLinesAndLoans = st.number_input("Open Credit Lines", 0, 50, 5)
NumberRealEstateLoansOrLines = st.number_input("Real Estate Loans", 0, 10, 1)
NumberOfDependents = st.number_input("Dependents", 0, 10, 2)

if st.button("Predict Risk"):

    payload = {
        "RevolvingUtilizationOfUnsecuredLines": RevolvingUtilizationOfUnsecuredLines,
        "age": age,
        "NumberOfTime30_59DaysPastDueNotWorse": NumberOfTime30_59DaysPastDueNotWorse,
        "NumberOfTime60_89DaysPastDueNotWorse": NumberOfTime60_89DaysPastDueNotWorse,
        "NumberOfTimes90DaysLate": NumberOfTimes90DaysLate,
        "DebtRatio": DebtRatio,
        "MonthlyIncome": MonthlyIncome,
        "NumberOfOpenCreditLinesAndLoans": NumberOfOpenCreditLinesAndLoans,
        "NumberRealEstateLoansOrLines": NumberRealEstateLoansOrLines,
        "NumberOfDependents": NumberOfDependents
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        result = response.json()

        st.success(f"Risk Level: {result['risk_level']}")
        st.write(f"Default Probability: {result['default_probability']:.2f}")

        fig = create_gauge(result["default_probability"])
        st.plotly_chart(fig, use_container_width=True)


    except Exception as e:
        st.error(f"Error: {str(e)}")
