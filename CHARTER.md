# Project Charter

## Header
- Team size: 1 (Solo project)
- Estimated hours: 50 hours/person

## Team
- Name: Anshula Mahajan (Solo project)
- GitHub: anshulamahajanma2025-stack
- Email: anshula.mahajan_ma2025@ashoka.edu.in

## Project Title
House Price Prediction

## Section 1: Stakeholder
A prospective home buyer or real estate agent in 
Ames, Iowa looking to estimate fair market value 
of a residential property.

Note: This is a prototype and training exercise. 
It does not claim to generalize to Indian housing 
markets or support real lending decisions.

## Section 2: Main Outcome
- Target variable: SalePrice (USD)
- Source table: train.csv
- Source column: SalePrice
- Population/panel: 1,460 residential properties 
  sold in Ames, Iowa, USA between 2006 and 2010

## Project Question
Which features of a house (size, quality, location, 
and amenities) best predict its sale price in Ames, 
Iowa, and how accurately can we predict SalePrice 
using these features?

## Project Type
Predictive

## Dataset
- Name: House Prices - Advanced Regression Techniques
- Source: Kaggle
- Link: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
- Format: CSV (train.csv, test.csv)
- Size: 1460 training rows, 81 columns
- Kaggle access method: Manual download after login
- Login/access status: Data already downloaded and 
  available in Colab
- Probe script path: notebooks/house_price_prediction.ipynb
  (Cell 3 loads train.csv and prints shape as proof)

## Fallback Plan
If Kaggle dataset becomes inaccessible:
- Use California Housing dataset from sklearn
  (available directly in Python, no download needed)
- Same predictive approach applies

## Section 3: Baseline and Success Threshold
- Baseline model: Linear Regression
- Features: LotArea, OverallQual, GrLivArea, 
  BedroomAbvGr, TotalBsmtSF, GarageArea
- Baseline MAE: $24,541.69
- Success threshold: held-out MAE ≤ $20,000 
  versus Linear Regression baseline MAE $24,541.69
- Saved in: outputs/baseline_metric.json

## Section 5: Falsifiable Hypothesis
Houses with higher OverallQual (quality rating) 
and larger GrLivArea (living area) will have 
higher SalePrice. Specifically, a Random Forest 
model using all 80 features will achieve a 
held-out MAE at least 18% lower than the 
Linear Regression baseline ($24,541.69), 
reaching MAE ≤ $20,000.

## Section 6: Scope Limits
We will not:
- Make any causal claims about what drives house prices
- Make any real lending or loan approval decisions
- Claim that results generalize beyond Ames, Iowa 
  (2006-2010) to Indian or other housing markets
- Claim the model is production-ready

## Section 9: Reproducibility Commitment
- Run command: uv run main.py
- main.py runs the full analysis end to end
- Primary output: outputs/primary_metric.json 
  with a passed boolean
- Baseline output: outputs/baseline_metric.json
- README contains the exact run command
- All outputs reproducible from one clean run
