import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

st.title("📊 Customer Segmentation Dashboard")

# Load dataset
df = pd.read_csv("customer-segmentation.csv")

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# Select numeric columns
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

if len(numeric_columns) >= 2:
    st.subheader("Scatter Plot")

    x_axis = st.selectbox("Select X-axis", numeric_columns)
    y_axis = st.selectbox("Select Y-axis", numeric_columns, index=1)

    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        title=f"{x_axis} vs {y_axis}"
    )

    st.plotly_chart(fig, use_container_width=True)

# Show summary
st.subheader("Summary Statistics")
st.write(df.describe())