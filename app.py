
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load and train model
@st.cache_resource
def train_model():
    df = pd.read_csv("train (1).csv")
    features = ["LotArea", "OverallQual", "GrLivArea", 
                "BedroomAbvGr", "TotalBsmtSF", "GarageArea"]
    data = df[features + ["SalePrice"]].dropna()
    X = data[features]
    y = data["SalePrice"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model, features

model, features = train_model()

# App title
st.title("🏠 House Price Predictor")
st.write("Enter house details to get an estimated sale price.")

# Input sliders
lot_area = st.slider("Lot Area (sq ft)", 1000, 20000, 8000)
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.slider("Living Area (sq ft)", 500, 5000, 1500)
bedrooms = st.slider("Bedrooms", 1, 8, 3)
basement = st.slider("Basement Area (sq ft)", 0, 3000, 800)
garage = st.slider("Garage Area (sq ft)", 0, 1500, 400)

# Predict
input_data = pd.DataFrame([[lot_area, overall_qual, gr_liv_area,
                             bedrooms, basement, garage]],
                          columns=features)
prediction = model.predict(input_data)[0]

# Show prediction
st.markdown("---")
st.metric("💰 Predicted Sale Price", f"${prediction:,.0f}")

# Feature importance
st.markdown("---")
st.subheader("What drives the price?")
importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values("Importance", ascending=True)

fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(importance_df["Feature"], importance_df["Importance"], 
        color="steelblue")
ax.set_xlabel("Importance Score")
ax.set_title("Feature Importance")
st.pyplot(fig)
