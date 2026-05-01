# Project Charter

## Team
- Name: Anshula Mahajan
- GitHub: anshulamahajanma2025-stack

## Project Title
House Price Prediction

## Project Question
What features of a house best predict its sale price?

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

## Main Outcome
Sale price of a house (SalePrice column) in USD

## Main Metric
Mean Absolute Error (MAE) in USD

## Baseline
Linear Regression using features:
LotArea, OverallQual, GrLivArea, BedroomAbvGr, 
TotalBsmtSF, GarageArea
Baseline MAE: $24,541.69

## Success Criteria
Improve MAE below $20,000 using a better model 
(Random Forest or XGBoost)

## What We Are NOT Claiming
- This is not a causal study
- We are not claiming these features cause price changes
- Predictions may not generalize outside this dataset

## Plan
| Week | Task |
|------|------|
| Apr 26 | Data loaded, baseline done |
| Apr 28 | Charter approved |
| May 5  | Milestone submitted |
| May 10 | Better model built |
| May 15 | Final submission |
