import pandas as pd
 
# 1. Load data
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")
 
print("=== SALES PREVIEW ===")
print(sales.head())
print("\n=== CUSTOMERS PREVIEW ===")
print(customers.head())
 
# 2. Data information
print("\n=== SALES INFO ===")
print(sales.info())
print("\n=== CUSTOMERS INFO ===")
print(customers.info())
 
# 3. Check missing values and duplicates
print("\nMissing values in Sales:\n", sales.isnull().sum())
print("\nMissing values in Customers:\n", customers.isnull().sum())
 
print("\nDuplicated rows in Sales:", sales.duplicated().sum())
print("Duplicated rows in Customers:", customers.duplicated().sum())
 
# 4. Add TotalValue column (transaction value)
sales["TotalValue"] = sales["Quantity"] * sales["UnitPrice"]
 
print("\n=== SALES WITH TOTAL VALUE ===")
print(sales.head())
 
# 5. Merge sales data with customers
merged = pd.merge(sales, customers, on="CustomerID", how="left")
 
print("\n=== MERGED DATA ===")
print(merged.head())
 
# 6. Basic statistics
print("\n=== SALES DESCRIBE ===")
print(sales["TotalValue"].describe())
 
# 7. Group analysis
# a) Sales by regions
region_sales = merged.groupby("Region")["TotalValue"].sum().reset_index()
print("\n=== SALES BY REGION ===")
print(region_sales)
 
# b) Sales by category
category_sales = merged.groupby("Category")["TotalValue"].sum().reset_index()
print("\n=== SALES BY CATEGORY ===")
print(category_sales)
 
# c) Top 3 customers by sales
top_customers = merged.groupby(["CustomerID", "Name"])["TotalValue"].sum().reset_index()
top_customers = top_customers.sort_values("TotalValue", ascending=False).head(3)
print("\n=== TOP 3 CUSTOMERS ===")
print(top_customers)
 
# 8. Add customer segment
def segment(value):
    if value > 5000:
        return "Premium"
    elif value > 2000:
        return "Standard"
    else:
        return "Basic"
 
customer_sales = merged.groupby("CustomerID")["TotalValue"].sum().reset_index()
customer_sales["Segment"] = customer_sales["TotalValue"].apply(segment)
 
print("\n=== CUSTOMER SEGMENTS ===")
print(customer_sales)
 
# 9. Sort customers by purchase value
sorted_customers = customer_sales.sort_values("TotalValue", ascending=False)
print("\n=== SORTED CUSTOMERS ===")
print(sorted_customers)
 
# 10. Save clean file for Power BI
merged.to_csv("clean_sales_data.csv", index=False)
print("\nFile clean_sales_data.csv has been saved!")

