import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
from xlsxwriter import workbook
from CLI_main import analyze, cat_insights, Region_sales, top_product_cust, Top_10, visualize, save_report


st.title("📊 Sales Insights Dashboard")

upload = st.file_uploader("📂 Upload Sales CSV", type=["csv"])

if upload:
    df = pd.read_csv(upload)
    df = df.fillna(0)

    choice = st.radio("Choose Section:", ["Analyze", "Insights", "Visualize"])

    # ----------- Analyze -----------
    if choice == "Analyze":
        if st.button("Total Sales, Profit, Quantity"):
            summary = analyze(df)  # must return dataframe in cli_main
            st.dataframe(summary)

        if st.button("Sales by Region"):
            region = Region_sales(df)
            st.dataframe(region)

    # ----------- Insights -----------
    elif choice == "Insights":
        if st.button("Category & Sub-Category Insights"):
            cat, sub_cat = cat_insights(df)   # must return both dfs
            st.dataframe(cat)
            st.dataframe(sub_cat)

        if st.button("Top Product & Customer"):
            result = top_product_cust(df)   # must return string
            st.success(result)

        if st.button("Top 10 Products"):
            top10 = Top_10(df)
            st.dataframe(top10)

    # ----------- Visualize -----------
    elif choice == "Visualize":
        region_sales = Region_sales(df)
        top10 = Top_10(df)
        cat, _ = cat_insights(df)
        visualize(df, region_sales, top10, cat)
        st.success("✅ Charts saved successfully")

    # ---- Export final analyzed file ----
if st.button("📥 Generate & Download Report"):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        total_sales = analyze(df)
        region_sales = Region_sales(df)
        cat_sales, sub_cat = cat_insights(df)
        top_10 = Top_10(df)

        total_sales.to_excel(writer, sheet_name="Total", index=False) 
        region_sales.to_excel(writer, sheet_name="Region", index=False)
        cat_sales.to_excel(writer, sheet_name="Categories", index=False)
        sub_cat.to_excel(writer, sheet_name="Sub-Categories", index=False)


        top_10.to_excel(writer, sheet_name="Top10", index=False)

    buffer.seek(0)  # reset pointer
    st.download_button(
        label="📥 Download analyzed Excel report",
        data=buffer,
        file_name="analyzed_sales.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

