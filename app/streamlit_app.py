import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Credit Risk AI",
    page_icon="🏦",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align:center;'>Credit Risk AI System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>AI-powered loan approval and risk explanation engine</p>",
    unsafe_allow_html=True
)

# -----------------------------
# GAUGE CHART
# -----------------------------
def create_gauge(prob):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={"text": "Risk Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "black"},
            "steps": [
                {"range": [0, 30], "color": "lightgreen"},
                {"range": [30, 70], "color": "orange"},
                {"range": [70, 100], "color": "red"},
            ],
        }
    ))
    fig.update_layout(height=300)
    return fig


# -----------------------------
# INPUT UI (TWO COLUMNS)
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 35)
    DebtRatio = st.number_input("Debt Ratio", 0.0, 10.0, 0.3)
    MonthlyIncome = st.number_input("Monthly Income", 0.0, 100000.0, 5000.0)
    RevolvingUtilizationOfUnsecuredLines = st.number_input("Revolving Utilization", 0.0, 10.0, 0.5)
    NumberOfDependents = st.number_input("Dependents", 0, 10, 2)

with col2:
    NumberOfTime30_59DaysPastDueNotWorse = st.number_input("30-59 Days Late", 0, 20, 1)
    NumberOfTime60_89DaysPastDueNotWorse = st.number_input("60-89 Days Late", 0, 20, 0)
    NumberOfTimes90DaysLate = st.number_input("90+ Days Late", 0, 20, 0)
    NumberOfOpenCreditLinesAndLoans = st.number_input("Open Credit Lines", 0, 50, 5)
    NumberRealEstateLoansOrLines = st.number_input("Real Estate Loans", 0, 10, 1)


# -----------------------------
# PREDICT BUTTON
# -----------------------------
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
        # -----------------------------
        # PREDICT API CALL
        # -----------------------------
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()

        prob = result["default_probability"]
        risk = result["risk_level"]

        # -----------------------------
        # RISK BADGE
        # -----------------------------
        if risk == "Low Risk":
            st.success(f"🟢 {risk}")
        elif risk == "Medium Risk":
            st.warning(f"🟠 {risk}")
        else:
            st.error(f"🔴 {risk}")

        # -----------------------------
        # METRICS CARDS
        # -----------------------------
        colA, colB = st.columns(2)

        with colA:
            st.metric("Default Probability", f"{prob:.2f}")

        with colB:
            st.metric("Risk Level", risk)

        # -----------------------------
        # GAUGE CHART
        # -----------------------------
        st.plotly_chart(create_gauge(prob), use_container_width=True)

        # -----------------------------
        # SHAP EXPLANATION
        # -----------------------------
        try:
            explain_response = requests.post(
                "http://127.0.0.1:8000/explain",
                json=payload
            )

            explanation = explain_response.json()["explanation"]

            st.subheader("Top Risk Drivers")

            df_exp = pd.DataFrame(
                list(explanation.items())[:7],
                columns=["Feature", "Impact"]
            )

            fig = px.bar(
                df_exp,
                x="Impact",
                y="Feature",
                orientation="h",
                title="Feature Contribution to Decision"
            )

            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Explanation error: {str(e)}")

    except Exception as e:
        st.error(f"Prediction error: {str(e)}")