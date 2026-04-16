import streamlit as st
import pandas as pd
from analyzer import analyze_data, visualize_data

st.title("📊 Data Analyzer Dashboard")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.write(df.head())

    st.subheader("📊 Summary Statistics")
    summary = analyze_data(df)
    st.write(summary)

    st.subheader("📉 Visualizations")
    visualize_data(df)