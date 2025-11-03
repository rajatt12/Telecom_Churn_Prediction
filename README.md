# 📊 Telecom Customer Churn Prediction

A machine learning project that predicts whether a telecom customer is likely to churn based on their usage behavior and plan details.  
Built with **Python**, **Scikit-learn**, and **Streamlit**, this project demonstrates the complete workflow from **data generation** to **web app deployment**.

---

## 🚀 Overview
Telecom companies face significant revenue losses due to customer churn.  
This project uses synthetic customer data to build a **churn prediction model** using classification algorithms.  
The trained model is deployed as a **Streamlit web app** for interactive churn prediction.

---

## 🧠 Key Features

### 📄 1. Synthetic Dataset Creation
- Generates a dataset of **300 telecom users** with realistic attributes:
  - `age`
  - `usage_gb`
  - `complaints`
  - `tenure_months`
  - `plan_type` (Prepaid/Postpaid)
- Simulates a **churn label** based on logical customer behavior patterns:
  - High complaints + Low tenure + Low usage → Higher churn probability.

---

### 🧹 2. Data Cleaning & Preprocessing
- Handles missing data using **SimpleImputer**:
  - Numeric values → Median
  - Categorical values → Most Frequent
- Encodes `plan_type` as:
   - Prepaid
   - Postpaid
- Ensures the dataset is clean, consistent, and ready for model training.

---

### 🌳 3. Model Training & Evaluation
- Trains a **Decision Tree Classifier** to predict customer churn.
- Evaluates model performance using:
- **Accuracy Score**
- **Confusion Matrix**
- **Classification Report**
- Selects the best-performing model and saves it.

