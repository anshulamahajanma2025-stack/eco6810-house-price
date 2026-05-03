import pandas as pd
import numpy as np
import json
import os
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Create outputs folder
os.makedirs('outputs', exist_ok=True)

print("=== House Price Prediction ===")
print("Loading data...")

# Load data
train = pd.read_csv('data/train (1).csv')
print(f"Data loaded: {train.shape[0]} rows, {train.shape[1]} columns")

# Features
features = ['LotArea', 'OverallQual', 'GrLivArea',
            'BedroomAbvGr', 'TotalBsmtSF', 'GarageArea']

data = train[features + ['SalePrice']].dropna()
X = data[features]
y = data['SalePrice']

# Split
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Baseline - Linear Regression
print("\nTraining baseline (Linear Regression)...")
baseline_model = LinearRegression()
baseline_model.fit(X_train, y_train)
baseline_preds = baseline_model.predict(X_val)
baseline_mae = mean_absolute_error(y_val, baseline_preds)
print(f"Baseline MAE: ${baseline_mae:,.2f}")

# Save baseline
baseline = {
    "metric_name": "MAE",
    "value": round(baseline_mae, 2),
    "unit": "USD"
}
with open('outputs/baseline_metric.json', 'w') as f:
    json.dump(baseline, f, indent=2)
print("Saved outputs/baseline_metric.json")

# Main model - Random Forest
print("\nTraining main model (Random Forest)...")
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_val)
rf_mae = mean_absolute_error(y_val, rf_preds)
print(f"Random Forest MAE: ${rf_mae:,.2f}")

# Save primary metric
threshold = 20000
passed = bool(rf_mae <= threshold)
primary = {
    "metric_name": "MAE",
    "value": round(rf_mae, 2),
    "threshold": threshold,
    "passed": passed
}
with open('outputs/primary_metric.json', 'w') as f:
    json.dump(primary, f, indent=2)
print("Saved outputs/primary_metric.json")

# Save milestone manifest
milestone = {
    "charter_locked": True,
    "sources": [
        {
            "name": "Kaggle House Prices Dataset",
            "status": "ok",
            "probe_artifact": "data/train (1).csv"
        }
    ],
    "baseline_ready": True,
    "primary_metric_schema_ready": True,
    "run_command": "uv run main.py"
}
with open('outputs/milestone_manifest.json', 'w') as f:
    json.dump(milestone, f, indent=2)
print("Saved outputs/milestone_manifest.json")

print("\n=== DONE ===")
print(f"Baseline MAE: ${baseline_mae:,.2f}")
print(f"Random Forest MAE: ${rf_mae:,.2f}")
print(f"Target threshold: ${threshold:,}")
print(f"Passed: {passed}")
