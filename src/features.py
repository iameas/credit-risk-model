import pandas as pd

def create_features(df):
    df = df.copy()

    df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].median())
    df["NumberOfDependents"] = df["NumberOfDependents"].fillna(df["NumberOfDependents"].median())

    df["Debt_to_Income"] = df["DebtRatio"] / (df["MonthlyIncome"] + 1)
    df["High_Utilization"] = (df["RevolvingUtilizationOfUnsecuredLines"] > 1).astype(int)

    return df