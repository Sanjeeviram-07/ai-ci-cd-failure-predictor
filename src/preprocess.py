# src/preprocess.py
import pandas as pd

df = pd.read_csv("data/raw/ci_cd_pipeline_failure_logs_dataset.csv")


# Create failure label (all 1s initially)
df["failed"] = 1

# Simulate successful runs by duplicating some rows
success_df = df.sample(frac=0.5, random_state=42).copy()

# Modify success rows to look like successful pipelines
success_df["failed"] = 0
success_df["failure_stage"] = None
success_df["failure_type"] = None
success_df["severity"] = "LOW"
success_df["retry_count"] = 0

# Combine failure + success
final_df = pd.concat([df, success_df], ignore_index=True)

# Select useful columns
cols = [
    "build_duration_sec",
    "test_duration_sec",
    "deploy_duration_sec",
    "cpu_usage_pct",
    "memory_usage_mb",
    "retry_count",
    "ci_tool",
    "language",
    "os",
    "cloud_provider",
    "severity",
    "failed"
]

final_df = final_df[cols]

final_df.to_csv("data/processed/cicd_logs_clean.csv", index=False)
print("✅ Preprocessed balanced dataset created")