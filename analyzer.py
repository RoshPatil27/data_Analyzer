import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def analyze_data(df):
    summary = {}

    # Basic info
    summary['Shape'] = df.shape
    summary['Columns'] = list(df.columns)

    # Statistics
    summary['Describe'] = df.describe()

    # Missing values
    summary['Missing Values'] = df.isnull().sum()

    return summary


def visualize_data(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numeric_cols:
        st.write(f"### 📌 {col}")

        fig, ax = plt.subplots()

        # Histogram
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

        # Boxplot
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=df[col], ax=ax2)
        st.pyplot(fig2)