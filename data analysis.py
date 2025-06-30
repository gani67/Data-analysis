# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the CSV file (replace with your actual filename)
df = pd.read_csv("sales_data.csv")  # Make sure the file is uploaded or in the same directory

# Step 3: Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: Check column names
print("\nColumns available:")
print(df.columns)

# Step 5: Group by Product and calculate total sales
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nTotal Sales by Product:")
print(product_sales)

# Step 6: Plot total sales by product
plt.figure(figsize=(10,6))
product_sales.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# Optional: Group by Region and plot
region_sales = df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(8,5))
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()
