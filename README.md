# 🛡️ Crypto Airdrop Fraud Detection ML

A clean, reproducible machine learning project for identifying suspicious wallet behavior in crypto airdrop ecosystems.

![status](https://img.shields.io/badge/status-active-success)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

---

## ✨ Why this project exists
Airdrops attract both genuine users and coordinated abuse. This repository demonstrates a practical fraud-detection workflow:

- collect wallet behavior features,
- assign suspicious labels,
- train/evaluate baseline models,
- communicate findings clearly.

It is designed to be understandable for readers, recruiters, and collaborators.

---

## 🧱 Repository structure

```text
.
├── 10k_airdrop_fraud_features_v1.csv             # Main dataset (10,000 wallets)
├── airdrop_fraud_detection_ml.ipynb              # Modeling notebook
├── data_preprocessing_wallet_behavior.ipynb      # Feature engineering + labeling notebook
├── docs/
│   └── PROJECT_OVERVIEW.md                       # Professional project narrative
├── scripts/
│   └── run_data_quality.py                       # CLI entrypoint for dataset quality checks
├── src/
│   └── crypto_airdrop_fraud_detection/
│       ├── __init__.py
│       └── data_quality.py                       # Reusable data-quality utilities (stdlib)
├── .env.example                                  # Environment variable template
├── .gitignore
├── requirements.txt
└── LICENSE
```

---

## 🚀 Quick start

### 1) Clone and install dependencies
```bash
git clone <your-repo-url>
cd crypto-airdrop-fraud-detection-ml
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Configure environment
```bash
cp .env.example .env
# then edit .env with your own values
```

### 3) Run a professional data-quality report
```bash
python scripts/run_data_quality.py --input 10k_airdrop_fraud_features_v1.csv --pretty
```

---

## 📊 Current dataset snapshot
The included dataset contains 10,000 rows and 11 columns, including the target label `is_suspicious`.

Core fields:
- wallet identity
- transaction volume/behavior
- activity age and diversity
- target label (`is_suspicious`)

---

## 🧠 Modeling notes
The notebooks currently implement a baseline pipeline with train/test split and classification metrics.

For production-quality improvements, recommended next steps are:
1. stronger external labels,
2. threshold tuning using precision/recall trade-offs,
3. model versioning + reproducible training scripts,
4. CI checks for data and code quality.

---

## 🎯 Professionalization checklist (done)
- [x] Added polished project README
- [x] Added reproducible dependency file
- [x] Added environment template
- [x] Added modular Python package folder
- [x] Added script-based data quality checks
- [x] Added project overview document for non-technical readers

---

## 📜 License
This project is licensed under the terms in `LICENSE`.
