import pandas as pd
import matplotlib.pyplot as plt
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

        # Histogram (matplotlib only)
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        st.pyplot(fig)

        # Boxplot
        fig2, ax2 = plt.subplots()
        ax2.boxplot(df[col], vert=False)
        st.pyplot(fig2)