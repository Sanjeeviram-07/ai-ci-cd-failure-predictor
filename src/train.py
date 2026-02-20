import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/processed/cicd_logs_clean.csv")

X = df.drop("failed", axis=1)
y = df["failed"]

num_features = [
    "build_duration_sec",
    "test_duration_sec",
    "deploy_duration_sec",
    "cpu_usage_pct",
    "memory_usage_mb",
    "retry_count"
]

cat_features = [
    "ci_tool",
    "language",
    "os",
    "cloud_provider",
    "severity"
]

preprocessor = ColumnTransformer([
    ("num", "passthrough", num_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
])

model = RandomForestClassifier(n_estimators=100, random_state=42)

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", model)
])

pipeline.fit(X, y)

joblib.dump(pipeline, "models/cicd_fail_model.pkl")
print("✅ Model trained and saved")

# Add to src/train.py after training
importances = pipeline.named_steps["model"].feature_importances_
print("Top features influencing failure prediction:", importances[:10])