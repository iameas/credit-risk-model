import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier


df = pd.read_csv("data/raw/cs-training.csv")
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

df.columns = df.columns.str.replace("-", "_")

df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].median())
df["NumberOfDependents"] = df["NumberOfDependents"].fillna(df["NumberOfDependents"].median())

X = df.drop(columns=["SeriousDlqin2yrs"])
y = df["SeriousDlqin2yrs"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=pos_weight,
        eval_metric="logloss",
        random_state=42
    ))
])

pipeline.fit(X_train, y_train)

joblib.dump({
    "model": pipeline,
    "features": list(X.columns)
}, "models/model_package.pkl")

print("Bulletproof model saved.")