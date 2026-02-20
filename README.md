# 🚀 AI CI/CD Failure Predictor (AI-Powered Quality Gate)

![CI Status](https://github.com/Sanjeeviram-07/ai-ci-cd-failure-predictor/actions/workflows/ci.yml/badge.svg)

An end-to-end **AI + DevOps (MLOps)** project that predicts CI/CD
pipeline failure risk using **Machine Learning** and integrates the
prediction as an **AI-powered quality gate** in GitHub Actions.\
The pipeline automatically blocks high-risk deployments and uploads
evaluation metrics as CI artifacts.\
The quality gate is also containerized using **Docker** for portable
execution.

------------------------------------------------------------------------

## 📌 Problem Statement

CI/CD pipelines often fail due to: - Build errors\
- Flaky tests\
- Environment issues\
- Resource constraints

Traditional pipelines react **after** failures occur.\
This project introduces an **AI-based proactive quality gate** that
predicts the probability of failure **before deployment** and blocks
risky releases automatically.

------------------------------------------------------------------------

## 🏗️ Architecture (High-Level)

    Kaggle CI/CD Logs
          ↓
    Data Preprocessing
          ↓
    ML Model Training (RandomForest + Preprocessing Pipeline)
          ↓
    Model Evaluation (Metrics + Confusion Matrix)
          ↓
    AI Quality Gate (Predict Failure Risk)
          ↓
    CI/CD (GitHub Actions) → Allow / Block Deployment
          ↓
    Docker Container (Portable Execution)

------------------------------------------------------------------------

## 🧰 Tech Stack

-   Python 3.10\
-   Scikit-learn\
-   Pandas\
-   GitHub Actions\
-   Docker\
-   Matplotlib, Seaborn

------------------------------------------------------------------------

## 🤖 AI-Powered CI/CD Quality Gate

Decision Logic: - **Risk ≥ Threshold** → ❌ Block deployment\
- **Risk \< Threshold** → ✅ Allow deployment

Configurable Environment Variables:

``` bash
FAILURE_THRESHOLD=0.8
DEMO_MODE=true
```

------------------------------------------------------------------------

## 🐳 Docker Support

Build image:

``` bash
docker build -t ai-ci-cd-failure-predictor .
```

Run container:

``` bash
docker run --rm -e DEMO_MODE=true -e FAILURE_THRESHOLD=0.8 ai-ci-cd-failure-predictor
```

------------------------------------------------------------------------

## 📁 Folder Structure

    ai-ci-cd-failure-predictor/
    ├── .github/
    │   └── workflows/
    │       └── ci.yml                 # GitHub Actions CI/CD pipeline
    │
    ├── data/
    │   ├── raw/
    │   │   └── cicd_logs_kaggle.csv   # Original dataset (Kaggle)
    │   └── processed/
    │       └── cicd_logs_clean.csv   # Cleaned dataset for training
    │
    ├── src/
    │   ├── preprocess.py             # Data cleaning & feature engineering
    │   ├── train.py                  # Model training pipeline
    │   ├── evaluate.py               # Evaluation + metrics + confusion matrix
    │   └── predict.py                # AI quality gate (CI blocking logic)
    │
    ├── models/
    │   └── cicd_fail_model.pkl       # Trained model artifact
    │
    ├── reports/
    │   ├── metrics.txt               # Classification report (CI artifact)
    │   └── confusion_matrix.png      # Confusion matrix plot (CI artifact)
    │
    ├── Dockerfile                    # Docker image for AI quality gate
    ├── requirements.txt              # Python dependencies
    ├── README.md                     # Project documentation
    ├── .gitignore                    # Git ignore rules
    └── Makefile                      # (Optional) DevOps automation shortcuts

------------------------------------------------------------------------

## 📦 CI Artifacts

-   `metrics.txt`\
-   `confusion_matrix.png`

------------------------------------------------------------------------

## ▶️ Run Locally

``` bash
pip install -r requirements.txt
python src/preprocess.py
python src/train.py
python src/evaluate.py
python src/predict.py
```

------------------------------------------------------------------------

## 👤 Author

**Sanjeeviram**

