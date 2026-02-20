# src/predict.py
import os
import sys
import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# =========================
# Config
# =========================
THRESHOLD = float(os.getenv("FAILURE_THRESHOLD", 0.8))
DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() == "true"  # true for demo, false for production

# =========================
# Load model
# =========================
MODEL_PATH = "models/cicd_fail_model.pkl"
if not os.path.exists(MODEL_PATH):
    print(f" Model not found at {MODEL_PATH}. Did training run?")
    sys.exit(1)

model = joblib.load(MODEL_PATH)

# =========================
# Demo Scenarios
# =========================
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
    "severity": "LOW",
}

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
    "severity": "CRITICAL",
}

def predict_one(sample: dict):
    X = pd.DataFrame([sample])
    proba = model.predict_proba(X)[0][1]  # probability of failure
    pred = int(proba >= THRESHOLD)
    return pred, proba

# =========================
# Run predictions (print both for demo)
# =========================
print(" SAFE scenario")
safe_pred, safe_proba = predict_one(safe_sample)
print(f" Failure Risk Probability: {safe_proba:.2f}")
print(" High Risk: FAIL" if safe_pred == 1 else " Low Risk: PASS")

print("\n RISKY scenario")
risky_pred, risky_proba = predict_one(risky_sample)
print(f" Failure Risk Probability: {risky_proba:.2f}")
print(" High Risk: FAIL" if risky_pred == 1 else " Low Risk: PASS")

# =========================
# Exit logic (controls CI)
# =========================
if DEMO_MODE:
    # Demo mode: CI PASS if SAFE is low-risk (shows green run)
    if safe_pred == 1:
        print("\n DEMO MODE: SAFE scenario flagged as risky (unexpected). Failing CI.")
        sys.exit(1)
    else:
        print("\n DEMO MODE: SAFE scenario passed. CI will PASS.")
        sys.exit(0)
else:
    # Production mode: CI FAIL if RISKY is high-risk (real quality gate)
    if risky_pred == 1:
        print("\n PROD MODE: Risk above threshold. Blocking deployment.")
        sys.exit(1)
    else:
        print("\n PROD MODE: Risk below threshold. Proceeding.")
        sys.exit(0)