import pandas as pd
import streamlit as st

def analyze_data(df):
    return {
        "Shape": df.shape,
        "Columns": list(df.columns),
        "Describe": df.describe(),
        "Missing Values": df.isnull().sum()
    }

def visualize_data(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numeric_cols:
        st.write(f"### {col}")

        # Streamlit built-in chart (no matplotlib needed)
        st.bar_chart(df[col])