# 🌟 Global Superstore Interactive Dashboard

## 📌 Project Description
This project is an **interactive Business Intelligence (BI) dashboard** built using **Streamlit** and **Plotly**, analyzing the **Global Superstore dataset**.  
The dashboard provides key insights into sales, profit, and top customers, allowing users to filter data by **Region**, **Category**, and **Sub-Category**.  

It is designed to help businesses understand performance trends, optimize product strategies, and identify top revenue-generating customers.

---

## Dataset
- Source: [Kaggle – Global Superstore Dataset](https://www.kaggle.com/datasets/fatihilhan/global-superstore-dataset)
- Format: CSV (`superstor.csv`)
- Rows: ~51,000+
- Columns include:
  - `sales`, `profit`, `quantity`, `discount`, `shipping_cost`
  - `region`, `category`, `sub_category`
  - `customer_name`, `order_date`, `ship_date`, `segment`
  - Plus other relevant order and product details  

---

## Task Objective
- Build a **fully interactive dashboard** using Streamlit.
- Enable filtering by:
  - Region
  - Category
  - Sub-Category
- Display KPIs:
  - Total Sales
  - Total Profit
  - Top 5 Customers by Sales
- Visualize performance using charts:
  - Sales by Region
  - Profit by Category
  - Sales by Sub-Category
  - Optional: Sales Trend Over Time  

---

## Approach / Methodology
1. **Data Cleaning**
   - Fixed column names (removed spaces & encoding issues)
   - Converted date columns to `datetime`
   - Ensured numeric columns are correct
   - Filled missing numeric values with 0
   - Dropped rows missing critical categorical information (`region`, `category`, `sub_category`, `customer_name`)  

2. **Exploratory Data Analysis (EDA)**
   - Checked data distribution
   - Calculated aggregated KPIs
   - Identified top 5 customers by sales  

3. **Dashboard Development**
   - Built with **Streamlit** for interactivity
   - Charts made with **Plotly Express**
   - Sidebar filters allow dynamic selection
   - KPIs and charts update automatically based on filters  

4. **Insights**
   - East region has the highest total sales
   - Certain product categories have high sales but lower profit → opportunity for cost optimization
   - Top customers contribute significantly to revenue → focus marketing efforts  

---

## Features
- Interactive filters: Region, Category, Sub-Category
- Key Performance Indicators (KPIs):
  - Total Sales
  - Total Profit
  - Top 5 Customers
- Charts:
  - Sales by Region
  - Profit by Category
  - Sales by Sub-Category
  - Optional: Sales Trend Over Time
- Responsive and easy-to-use interface  

---

## 🖥️ Dashboard Preview

### Main Dashboard
<img src="Images/Screenshot 2026-01-18 170915.png" width="800" alt="Main Dashboard Screenshot"/>

### Sales by Region
<img src="Images/Screenshot 2026-01-18 170950.png" width="800" alt="Sales by Region"/>

### Profit by Category
<img src="Images/Screenshot 2026-01-18 171016.png" width="800" alt="Profit by Category"/>

### Sales by Sub-Category
<img src="Images/Screenshot 2026-01-18 171042.png" width="800" alt="Sales by Sub-Category"/>

---



