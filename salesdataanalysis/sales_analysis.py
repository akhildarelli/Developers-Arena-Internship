import pandas as pd

df = pd.read_csv(r"C:\Users\USER\Desktop\salesdataanalysis\sales_data.csv")

df['Date'] = pd.to_datetime(df['Date'])

total_sales = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
highest_sale = df['Total_Sales'].max()
lowest_sale = df['Total_Sales'].min()

best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

print("========== SALES DATA ANALYSIS REPORT ==========")
print(f"Total Revenue        : ₹{total_sales:,.2f}")
print(f"Average Sale Value   : ₹{average_sales:,.2f}")
print(f"Highest Single Sale  : ₹{highest_sale:,.2f}")
print(f"Lowest Single Sale   : ₹{lowest_sale:,.2f}")
print(f"Best-Selling Product : {best_product}")
print("================================================")
