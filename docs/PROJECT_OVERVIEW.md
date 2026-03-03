# Project Overview

## Executive summary
This project studies airdrop-participant wallet behavior to detect suspicious activity patterns likely associated with abuse or bot-driven farming.

The current workflow uses:
- wallet-level feature construction,
- rule-based suspicious labeling,
- baseline supervised classification.

## Business value
A reliable fraud signal can help:
- reduce reward leakage to abusive actors,
- improve campaign fairness,
- increase trust in token distribution programs.

## Dataset details
Primary dataset: `10k_airdrop_fraud_features_v1.csv`
- Rows: 10,000
- Columns: 11
- Target: `is_suspicious`

## Method flow
1. **Collect** transaction-level wallet activity.
2. **Aggregate** into wallet-level features.
3. **Label** suspicious wallets with transparent rules.
4. **Train** baseline classifiers.
5. **Evaluate** and iterate.

## Risks and caveats
- Rule-based labels can encode assumptions and may not perfectly match real-world fraud.
- Class imbalance requires careful metric interpretation.
- Crypto behavior patterns can drift over time.

## Recommended roadmap
- Introduce externally validated labels where possible.
- Add temporal validation splits.
- Track experiments and model versions.
- Build lightweight inference API for scoring new wallets.
