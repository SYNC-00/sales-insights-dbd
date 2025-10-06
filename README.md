# 📊 Sales Insights Dashboard (CLI + Streamlit)

A dual-version **Python Data Analysis Project** that provides actionable **sales insights** through analytics and visualization.

Built using **Pandas, Matplotlib, Seaborn, and Streamlit**, this project showcases both a **command-line dashboard** and a **web-based Streamlit app**, making it perfect for **portfolios, freelancing, and analytics roles**.

---

## 🧩 Project Overview

| Version | Description | Run Command |
|----------|--------------|--------------|
| **🖥️ CLI Dashboard** | Text-based analytics app that runs in the terminal. | `python CLI_main.py` |
| **🌐 Streamlit Dashboard** | Web-based interactive app with charts and file upload. | `streamlit run main_app.py` |

---

## ⚙️ Features

### 🔹 Common Features (Both Versions)
- Load & clean CSV data (handles NaN → 0)
- Calculate total **Sales, Profit, Quantity**
- Analyze **Category**, **Sub-Category**, and **Region**-wise performance
- Identify **Top Products** & **Top Customers**
- Generate a complete **Excel report** with insights
- Visualize results (Bar, Pie, and Heatmap charts)

---

### 🖥️ CLI Version

#### Run Locally
```bash
python CLI_main.py

---

### Key Highlights

Uses Colorama and Tabulate for clean formatted outputs.

Saves visualizations automatically (.png files).

Generates an Excel report (analyzed_sales.xlsx) with:

Total Summary

Category Summary

Sub-Category Summary

Region Summary

Top 10 Products

Top Product & Customer

---

## 🌐 Streamlit Version

### Run locally 
streamlit run main_app.py

---

### Web Dashboard Features-

Upload any sales dataset (.csv file).

Choose between three sections:

Analyze: View totals and region performance.

Insights: View categories, top products, and customers.

Visualize: Auto-generate charts and export them.

Download a complete Excel report directly

---

### Example Layout-
📊 Sales Insights Dashboard
 ┣ 📂 Upload CSV
 ┣ 🔘 Analyze
 ┣ 🔘 Insights
 ┣ 🔘 Visualize
 ┗ 📥 Download Report

###📊 Visualizations

- Bar Chart: Sales by Region

- Bar Chart: Top 10 Products

- Pie Chart: Category-wise Sales

- Heatmap: Region vs Category Performance

---

## 📦 Installation
1. Clone the repo and install all dependencies:
git clone https://github.com/yourusername/sales-insights-dashboard.git
cd sales-insights-dashboard

2. Install dependencies:
pip install -r requirements.txt

3. Run either version: 
python CLI_main.py

       or

streamlit run main_app.py


---

### 🧠 Tech Stack
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Colorama
- Tabulate
- XlsxWriter

---

📸 Output Preview:

