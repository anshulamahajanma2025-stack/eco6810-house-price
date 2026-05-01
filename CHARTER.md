# Project Charter

## Team
- Name: Anshula Mahajan (Solo project)
- GitHub: anshulamahajanma2025-stack
- Email: anshula.mahajan_ma2025@ashoka.edu.in

## Project Title
House Price Prediction

## Project Question
Which features of a house (size, quality, location, 
and amenities) best predict its sale price, and how 
accurately can we predict the sale price using 
these features?

## Stakeholder
Home buyers, banks, and real estate agents who need 
accurate price estimates for decision making.

## Project Type
Predictive

## Dataset
- Name: House Prices - Advanced Regression Techniques
- Source: Kaggle
- Link: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
- Format: CSV (train.csv, test.csv)
- Size: 1460 training rows, 81 columns
- Access/Probe path: notebooks/house_price_prediction.ipynb
  (Cell 3 loads train.csv and prints shape as proof)

## Main Outcome
Sale price of a house (SalePrice column) in USD

## Main Metric
Mean Absolute Error (MAE) in USD

## Baseline
Model: Linear Regression
Features used: LotArea, OverallQual, GrLivArea, 
BedroomAbvGr, TotalBsmtSF, GarageArea
Baseline MAE: $24,541.69
Saved in: outputs/baseline_metric.json

## Success Metric / Threshold
Target: MAE below $20,000 using Random Forest or XGBoost
This means at least 18% improvement over baseline.

## Fallback Plan
If Kaggle dataset becomes inaccessible:
- Use California Housing dataset from sklearn
  (available directly in Python, no download needed)
- Same predictive approach applies

## What We Are NOT Claiming
- This is not a causal study
- We are not claiming these features cause price changes
- Predictions may not generalize outside this dataset

## Plan
| Date | Task |
|------|------|
| Apr 26 | Data loaded, baseline done |
| May 1  | Charter revised and resubmitted |
| May 5  | Milestone submitted |
| May 10 | Better model built |
| May 15 | Final submission |
