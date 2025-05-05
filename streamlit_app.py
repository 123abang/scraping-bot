import streamlit as st
import pandas as pd

# Make the app take the full browser width
st.set_page_config(layout="wide", page_title="UK Logistics Companies")

st.title("📦 UK Logistics Companies Directory")

# 1. Load your full CSV
df = pd.read_csv("uk_logistics_companies.csv")

# 2. (Optional) Inspect what columns you actually have
st.write("**Columns in dataset:**", df.columns.tolist())

# 3. Sidebar filters (to let users toggle phone/website visibility)
st.sidebar.header("Filter options")
show_only_with_phone   = st.sidebar.checkbox("Only companies with phone", False)
show_only_with_website = st.sidebar.checkbox("Only companies with website", False)

filtered = df.copy()
if show_only_with_phone:
    filtered = filtered[filtered["phone"].str.strip().astype(bool)]
if show_only_with_website:
    filtered = filtered[filtered["website"].str.strip().astype(bool)]

# 4. Display the DataFrame with just the four fields you care about
st.dataframe(
    filtered[["name", "address", "phone", "website"]],
    width=1000,  # you can tweak this
    height=600
)
