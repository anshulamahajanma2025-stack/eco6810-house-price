# Final Report

## 1. Question
Which features of a house best predict its sale 
price in Ames, Iowa, and how accurately can we 
predict SalePrice using these features?

The target stakeholder is a prospective home buyer 
or real estate agent in Ames, Iowa who needs to 
estimate fair market value of a property. This is 
a prototype and training exercise. It does not 
claim to generalize to Indian housing markets or 
support real lending decisions.

## 2. Charter Summary
- Project type: Predictive
- Main metric: Mean Absolute Error (MAE) in USD
- Success threshold: held-out MAE ≤ $20,000
- Baseline: Linear Regression MAE = $24,541.69

## 3. Data
- Source: Kaggle House Prices - Advanced Regression 
  Techniques dataset
- Access: Manual download after Kaggle login
- Training set: 1,460 residential properties sold 
  in Ames, Iowa between 2006 and 2010
- Features used: LotArea, OverallQual, GrLivArea, 
  BedroomAbvGr, TotalBsmtSF, GarageArea
- Target variable: SalePrice (USD)
- No source failures or fallbacks were needed

## 4. Method
**Baseline:** A Linear Regression model was trained 
on 6 features using an 80/20 train/validation split 
with random_state=42.

**Main model:** A Random Forest with 100 trees was 
trained on the same 6 features and same split. 
Evaluation metric is MAE on the held-out 20% 
validation set.

## 5. Result
- Main metric value: $19,409.73
- Threshold: $20,000
- Passed: ✅ Yes

The Random Forest model achieved a held-out MAE of 
$19,409.73, which is a 20.9% improvement over the 
Linear Regression baseline of $24,541.69. This 
means on average the model's price estimate is 
off by about $19,410 per house.

## 6. Evidence
- Figure 1: Distribution of house sale prices 
  (outputs/figure1_price_distribution.png)
- Figure 2: Baseline vs Random Forest MAE comparison 
  (outputs/figure2_model_comparison.png)
- Figure 3: Feature importance scores 
  (outputs/figure3_feature_importance.png)

OverallQual is the strongest predictor with an 
importance score of ~0.59. GrLivArea is second 
at ~0.20. BedroomAbvGr has the least predictive 
power at ~0.01.

## 7. Limits
- Only 6 out of 80 available features were used
- Results apply only to Ames, Iowa (2006-2010)
- No causal claims are made about what drives prices
- Model is not suitable for real lending decisions
- Predictions may not generalize to other cities 
  or time periods including Indian housing markets

## 8. If The Result Was Null Or Weak
The result was not null. The Random Forest passed 
the threshold. However, an MAE of ~$19,410 means 
meaningful error remains. Using all 80 features 
would likely improve performance further.

## 9. Reproducibility
- Run command: uv run main.py
- Runtime: approximately 30 seconds
- Output files written:
  - outputs/baseline_metric.json
  - outputs/primary_metric.json
  - outputs/milestone_manifest.json
  - outputs/figure1_price_distribution.png
  - outputs/figure2_model_comparison.png
  - outputs/figure3_feature_importance.png

## 10. AI Usage
AI was used for initial code structure and 
formatting help. All results, numbers, and 
outputs were verified manually.
See [AI_USAGE_LOG.md](./AI_USAGE_LOG.md) 
for the detailed log.
