import pandas as pd 

#Step 1: Load the dataset
df =pd.read_csv (r"C:\Users\joges\Downloads\sales_data.csv")

#Step 2: Explore the data
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nData Types:\n", df.dtypes)
 
#Step 3:Clean the data
#Check missing values
df.fillna(0, inplace=True)

#Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 4: Analyze sales
# Calculate total sales if not already present
if 'Total_Sales' not in df.columns:
    df['Total_Sales'] = df['Quantity'] * df['Price']
    
total_revenue = df['Total_Sales'].sum()
average_order_value = df['Total_Sales'].mean()
total_units_sold = df['Quantity'].sum()

#Best selling product
best_selling_product =(
     df.groupby('Product')['Total_Sales']
     .sum()
     .idxmax()
)

# Step 5: Output results
print("\n SALES ANALYSIS REPORT")
print("-" * 30)
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Average Order Value: {average_order_value:,.2f}")
print(f"Total Units Sold: {total_units_sold}")
print(f"Best Selling Product: {best_selling_product}")


