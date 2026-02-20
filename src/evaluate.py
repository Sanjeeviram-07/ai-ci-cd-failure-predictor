# src/evaluate.py
import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Create reports directory
os.makedirs("reports", exist_ok=True)

# Load processed dataset
df = pd.read_csv("data/processed/cicd_logs_clean.csv")

# Features & target
X = df.drop("failed", axis=1)
y = df["failed"]

# Load trained pipeline model
model = joblib.load("models/cicd_fail_model.pkl")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Predict
y_pred = model.predict(X_test)

# Console output
print("\n Model Evaluation Report:\n")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("\n Confusion Matrix:\n")
print(cm)

# Save metrics to file
report_text = classification_report(y_test, y_pred)
with open("reports/metrics.txt", "w") as f:
    f.write("Classification Report\n")
    f.write(report_text)

# Save confusion matrix image
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("reports/confusion_matrix.png")

print("\n Reports saved to:")
print(" - reports/metrics.txt")
print(" - reports/confusion_matrix.png")