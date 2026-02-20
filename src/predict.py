# # src/predict.py
# import joblib
# import pandas as pd
# import sys

# # Load trained model
# model = joblib.load("models/cicd_fail_model.pkl")

# #  Simulated current pipeline metrics (you can later replace with real values)
# sample = {
#     "build_duration_sec": 600,
#     "test_duration_sec": 400,
#     "deploy_duration_sec": 300,
#     "cpu_usage_pct": 78.5,
#     "memory_usage_mb": 4200,
#     "retry_count": 2,
#     "ci_tool": "Jenkins",
#     "language": "Python",
#     "os": "ubuntu-latest",
#     "cloud_provider": "AWS",
#     "severity": "CRITICAL"
# }

# # Convert to DataFrame
# X_new = pd.DataFrame([sample])

# # Predict failure risk
# pred = model.predict(X_new)[0]
# proba = model.predict_proba(X_new)[0][1]  # probability of failure

# print(f" Failure Risk Probability: {proba:.2f}")

# if pred == 1:
#     print(" High Risk: Pipeline likely to FAIL. Blocking deployment.")
#     sys.exit(1)   # Fail CI job
# else:
#     print(" Low Risk: Pipeline likely to PASS. Safe to proceed.")
# src/predict.py
import os
import joblib
import pandas as pd
import sys

model = joblib.load("models/cicd_fail_model.pkl")
THRESHOLD = float(os.getenv("FAILURE_THRESHOLD", 0.8))
# 🔹 Scenario A: Low-risk (should PASS)
safe_sample = {
    "build_duration_sec": 200,
    "test_duration_sec": 150,
    "deploy_duration_sec": 100,
    "cpu_usage_pct": 35.0,
    "memory_usage_mb": 1500,
    "retry_count": 0,
    "ci_tool": "GitHub Actions",
    "language": "Python",
    "os": "ubuntu-latest",
    "cloud_provider": "On-Prem",
    "severity": "LOW"
}

# 🔹 Scenario B: High-risk (should FAIL)
risky_sample = {
    "build_duration_sec": 900,
    "test_duration_sec": 700,
    "deploy_duration_sec": 500,
    "cpu_usage_pct": 88.0,
    "memory_usage_mb": 6000,
    "retry_count": 3,
    "ci_tool": "Jenkins",
    "language": "Python",
    "os": "ubuntu-latest",
    "cloud_provider": "AWS",
    "severity": "CRITICAL"
}

for name, sample in [("SAFE", safe_sample), ("RISKY", risky_sample)]:
    X_new = pd.DataFrame([sample])
    proba = model.predict_proba(X_new)[0][1]
    pred = model.predict(X_new)[0]

    print(f"\n {name} scenario")
    print(f" Failure Risk Probability: {proba:.2f}")

    # After getting proba
if proba >= THRESHOLD:
    print(f" Risk {proba:.2f} >= threshold {THRESHOLD}. Blocking deployment.")
    sys.exit(1)
else:
    print(f" Risk {proba:.2f} < threshold {THRESHOLD}. Proceeding.")
# Exit with status based on SAFE scenario (for PASS demo)
# sys.exit(1 if model.predict(pd.DataFrame([safe_sample]))[0] == 1 else 0)
# Demo PASS: exit based on SAFE scenario
sys.exit(1 if model.predict(pd.DataFrame([safe_sample]))[0] == 1 else 0)