import streamlit as st
import pandas as pd
import joblib

# --- Load Model ---
model = joblib.load("churn_decision_tree.joblib")

# --- Page Setup ---
st.title("📊 Telecom Customer Churn Prediction")
st.write("Enter customer details below to predict if they are likely to churn.")

# --- Input Fields ---
age = st.number_input("Age", min_value=18, max_value=100, value=28)
usage_gb = st.number_input("Monthly Data Usage (GB)", min_value=0.0, max_value=1000.0, value=6.0)
complaints = st.number_input("Number of Complaints", min_value=0, max_value=1000, value=2)
tenure_months = st.number_input("Tenure (in months)", min_value=0, max_value=120, value=4)
plan_type = st.selectbox("Plan Type", ["Prepaid", "Postpaid"])

# Encode categorical input
plan_type_enc = 0 if plan_type == "Prepaid" else 1

# --- Predict Button ---
if st.button("🔍 Predict Churn"):
    # Create input DataFrame
    new_data = pd.DataFrame([{
        "age": age,
        "usage_gb": usage_gb,
        "complaints": complaints,
        "tenure_months": tenure_months,
        "plan_type_enc": plan_type_enc
    }])
    
    # Make prediction
    prediction = model.predict(new_data)[0]
    
    # --- Display Result ---
    if prediction == 1:
        st.error("⚠️ The customer is likely to CHURN.")
    else:
        st.success("✅ The customer is NOT likely to churn.")

