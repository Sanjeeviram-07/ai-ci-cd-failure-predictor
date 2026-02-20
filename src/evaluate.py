# src/evaluate.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load processed dataset
df = pd.read_csv("data/processed/cicd_logs_clean.csv")

# Features & target
X = df.drop("failed", axis=1)
y = df["failed"]

# Load trained pipeline model
model = joblib.load("models/cicd_fail_model.pkl")

# Split data (same split idea as training for fair evaluation)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Predict on test set
y_pred = model.predict(X_test)

# Print evaluation metrics
print("\n📊 Model Evaluation Report:\n")
print(classification_report(y_test, y_pred))

print("\n🧩 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))