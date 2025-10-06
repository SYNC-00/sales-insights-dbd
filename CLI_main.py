import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore,Style,init
import seaborn as sns
from tabulate import tabulate

print(Fore.BLUE + "Sales Insights Dashboard")

def load_file():
    filename = input("Enter ur CSV file: ")
    if not filename.endswith(".csv"):
        print(Fore.RED + "❌ Error! PLease enter a  valid csv file")
        return None
    try:
        df = pd.read_csv(filename)
        df = df.fillna(0)
        print(Fore.GREEN + "✅ File loaded successfully")
        return df
    except FileNotFoundError:
        print(Fore.RED + "❌ Invalid File. Please check if the file is valid")
        return None

def analyze(df):
    Total_summary = df[["Quantity", "Sales", "Profit"]].sum().reset_index()
    Total_summary.columns = ["Metrics", "Values"]
    print(tabulate(Total_summary, headers=["Metrics", "Values"], tablefmt="pretty"))
    return Total_summary


def cat_insights(df):
        Cat_insights = df.groupby("Category")[["Sales", "Profit", "Quantity"]].sum().reset_index()
        sub_cat = df.groupby("Sub-Category")[["Sales", "Profit", "Quantity"]].sum().reset_index()
        print("Category Insights\n")
        print(tabulate(Cat_insights, headers="keys", tablefmt="pretty"))
        print("\nSub-Category")
        print(tabulate(sub_cat, headers="keys", tablefmt="pretty"))
        return Cat_insights, sub_cat

#Sales by Region
def Region_sales(df):
         region_sales = df.groupby("Region")[["Sales", "Profit", "Quantity"]].sum().reset_index()
         print(tabulate(region_sales, headers="keys", tablefmt="pretty"))
         return region_sales
    
#TOp product and customer
def top_product_cust(df):
    top = df["Quantity"].idxmax()
    top_pro = df.loc[top, "Product Name"]
    top_quant = df.loc[top, "Quantity"]
    top_cust = df.loc[top, "Customer Name"]
    print(f"The Top Product is {top_pro} with {top_quant} units sold")
    print(f"The Top Customer is none other than {top_cust}")
    return f"**The top product is:** {top_pro} with {top_quant} units sold  \n**The top customer is:** {top_cust}"


#TOp 10 Products
def Top_10(df):
    top_10 = df.sort_values(by="Sales", ascending=False).head(10)
    table = top_10[["Product Name", "Sales"]]
    print("The Top 10 Products are:")
    print(tabulate(table.values, headers=table.columns, tablefmt="pretty"))
    
    return top_10

def save_report(df):
    # Collect results
    total_summary = df[["Quantity", "Sales", "Profit"]].sum().reset_index()
    total_summary.columns = ["Metric", "Value"]

    cat_summary = df.groupby("Category")[["Sales", "Profit", "Quantity"]].sum().reset_index()
    sub_summary = df.groupby("Sub-Category")[["Sales", "Profit", "Quantity"]].sum().reset_index()
    region_summary = df.groupby("Region")[["Sales", "Profit", "Quantity"]].sum().reset_index()

    top_10 = df.sort_values(by="Sales", ascending=False).head(10)

    # Top product and customer
    top = df["Quantity"].idxmax()
    top_pro = df.loc[top, "Product Name"]
    top_quant = df.loc[top, "Quantity"]
    top_cust = df.loc[top, "Customer Name"]
    top_cust_df = pd.DataFrame({
        "Top Product": [top_pro],
        "Quantity Sold": [top_quant],
        "Top Customer": [top_cust]
    })

    # Save everything into one Excel file with multiple sheets
    with pd.ExcelWriter("analyzed_sales.xlsx") as writer:
        total_summary.to_excel(writer, sheet_name="Total Summary", index=False)
        cat_summary.to_excel(writer, sheet_name="Category Summary", index=False)
        sub_summary.to_excel(writer, sheet_name="Sub-Category Summary", index=False)
        region_summary.to_excel(writer, sheet_name="Region Summary", index=False)
        top_10.to_excel(writer, sheet_name="Top 10 Products", index=False)
        top_cust_df.to_excel(writer, sheet_name="Top Product & Customer", index=False)

    print(Fore.GREEN + "✅ Saved full insights report as analyzed_sales.xlsx")




def visualize(df, region_sales, top_10, Cat_insights):
    #Bar
    plt.figure(figsize=(5,4)) 
    plt.bar(region_sales["Region"], region_sales["Sales"], color="red")
    plt.title("Sales By Region Chart")
    plt.xlabel("Region")
    plt.ylabel("sales")
    plt.savefig("Sales_by_region.png")
    plt.close()


    #BAr 2
    plt.figure(figsize=(12,5))
    plt.bar(top_10["Product Name"], top_10["Sales"], color="green")
    plt.title("Top 10 Products Chart")
    plt.xlabel("Products")
    plt.ylabel("Sales")
    plt.savefig("Top_10_products.png")
    plt.close()

    
    #pie chart
    plt.figure()
    cat = Cat_insights.groupby("Category")["Sales"].sum()
    plt.pie(cat.values, labels=cat.index, autopct="%1.1f%%", startangle=90)
    plt.title("Categoru-wise Sales Chart") 
    plt.savefig("Category_wise_sales.png")
    plt.close()

   #heatmap
   # made pivot table  as it creates the grid (Region × Category with sales)(To restructure data)
    pivot = df.pivot_table(index="Region", columns="Category", values="Sales", aggfunc="sum") 
    plt.figure(figsize=(8,6))
    sns.heatmap(pivot, annot=True,fmt=".0f", cmap="YlGnBu") #used fmt=".0f", as it removes decimals nd keeps clean integers
    plt.title("Region Vs Category Sales Heatmap")
    plt.savefig("region_cat_sales.png")
    plt.close()


def main():
     df = load_file()
     if df is None:
          return
     while True:
             print(Fore.MAGENTA + "1. Analyze")
             print(Fore.MAGENTA + "2. Category & Sub-Category Insights")
             print(Fore.MAGENTA + "3. Sales by region")
             print(Fore.MAGENTA + "4. Top Product & Customer")
             print(Fore.MAGENTA + "5. Top 10 Products")
             print(Fore.MAGENTA + "6. Visualize")
             print(Fore.MAGENTA + "7. Save Report")
             print(Fore.MAGENTA + "8. Exit")
             choice = input(Fore.MAGENTA + "Select any option:")

             if choice == "1":
                   analyze(df)
             elif choice == "2":
                  Cat_insights = cat_insights(df)
             elif choice == "3":
                  region_sales = Region_sales(df)
             elif choice == "4":
                  top_product_cust(df)
             elif choice == "5":
                  top_10 = Top_10(df)
             elif choice == "6":
                  region_sales = Region_sales(df)
                  top_10 = Top_10(df)
                  Cat_insights, sub_cat = cat_insights(df)
                  visualize(df, region_sales, top_10, Cat_insights)
                  print(Fore.GREEN + "✅ Charts saved successfully")
             elif choice == "7":
                  save_report(df)
             elif choice == "8":
                  print(Fore.CYAN + "Exiting!!!")

             else:
                  print(Fore.RED + "❌ Invalid choice! Please try again")
                  continue
                  
if __name__ == "__main__":
     main()
