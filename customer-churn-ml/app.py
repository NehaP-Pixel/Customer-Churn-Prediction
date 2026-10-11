import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model and Dataset
# -----------------------------

model = joblib.load("models/churn_model.pkl")

df = pd.read_csv("data/raw/customer_churn_10000.csv")

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("📊 Customer Churn Prediction System")
st.write("Intelligent Customer Risk Analysis Dashboard")

# -----------------------------
# Dashboard
# -----------------------------

st.header("📈 Customer Dashboard")

total_customers = len(df)

churn_customers = int(df["Churn"].sum())

retained_customers = total_customers - churn_customers

average_churn_probability = df["Churn"].mean() * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    total_customers
)

col2.metric(
    "Predicted Churn Customers",
    churn_customers
)

col3.metric(
    "Retained Customers",
    retained_customers
)

col4.metric(
    "Average Churn Probability",
    f"{average_churn_probability:.2f}%"
)

# -----------------------------
# Existing Risk Summary
# -----------------------------

st.header("⚠️ Risk Summary")

high_risk = int((df["Churn"] == 1).sum())
medium_risk = 0

col5, col6 = st.columns(2)

col5.metric(
    "High-Risk Customers",
    high_risk
)

col6.metric(
    "Medium-Risk Customers",
    medium_risk
)

# -----------------------------
# Dataset Preview
# -----------------------------

st.header("👥 Customer Data")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.success("Dashboard loaded successfully! 🎉")