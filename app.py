import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Global Superstore Dashboard",
    layout="wide"
)

st.title(" Global Superstore Interactive Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("superstore.csv", encoding="latin1")

    # Clean column names
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace(".", "_")

    # Rename broken column
    df.rename(columns={'è®°å½æ°': 'row_count'}, inplace=True)

    # Convert dates
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

    # Numeric columns
    numeric_cols = ['sales', 'profit', 'quantity', 'discount', 'shipping_cost']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Drop critical missing values
    df.dropna(subset=['region', 'category', 'sub_category', 'customer_name'], inplace=True)

    return df

df = load_data()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df['region'].unique()),
    default=sorted(df['region'].unique())
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df['category'].unique()),
    default=sorted(df['category'].unique())
)

selected_sub_category = st.sidebar.multiselect(
    "Select Sub-Category",
    options=sorted(df['sub_category'].unique()),
    default=sorted(df['sub_category'].unique())
)

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_df = df[
    (df['region'].isin(selected_region)) &
    (df['category'].isin(selected_category)) &
    (df['sub_category'].isin(selected_sub_category))
]

# -----------------------------
# KPIs
# -----------------------------
total_sales = filtered_df['sales'].sum()
total_profit = filtered_df['profit'].sum()

top_5_customers = (
    filtered_df.groupby('customer_name')['sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

st.subheader(" Key Performance Indicators")

col1, col2 = st.columns(2)
col1.metric(" Total Sales", f"${total_sales:,.0f}")
col2.metric(" Total Profit", f"${total_profit:,.0f}")

st.subheader("Top 5 Customers by Sales")
st.dataframe(top_5_customers)

# -----------------------------
# CHARTS
# -----------------------------
st.subheader("Sales by Region")
sales_by_region = filtered_df.groupby('region')['sales'].sum().reset_index()
fig1 = px.bar(sales_by_region, x='region', y='sales')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Profit by Category")
profit_by_category = filtered_df.groupby('category')['profit'].sum().reset_index()
fig2 = px.bar(profit_by_category, x='category', y='profit')
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Sales by Sub-Category")
sales_by_subcat = filtered_df.groupby('sub_category')['sales'].sum().reset_index()
fig3 = px.bar(sales_by_subcat, x='sub_category', y='sales')
st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("**Built by Sadain Sikandar | Global Superstore BI Dashboard**")
