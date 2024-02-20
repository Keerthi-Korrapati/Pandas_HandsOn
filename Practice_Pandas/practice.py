import pandas as pd

# Load data from CSV file
sales_data = pd.read_csv('sales_data.csv')

# Display the first few rows of the DataFrame
print("First few rows of the sales data:")
print(sales_data.head())

# Data Cleaning
# Check for missing values
print("\nNumber of missing values in each column:")
print(sales_data.isnull().sum())

# Remove duplicates if any
sales_data = sales_data.drop_duplicates()

print("\nSummary statistics of sales data:")
print(sales_data.describe()) # It gives aggregations of data 

# Sales Trends Analysis
# Convert 'Date' column to datetime format
sales_data['Date'] = pd.to_datetime(sales_data['Date'])


# Extract month and year from 'Date' column
sales_data['Month'] = sales_data['Date'].dt.month
sales_data['Year'] = sales_data['Date'].dt.year

# Group by month and year, and calculate total sales revenue
monthly_sales = sales_data.groupby(['Year', 'Month'])['Sales'].sum()
print("\nMonthly sales trends:")
print(monthly_sales)

# Top-Selling Products
top_products = sales_data.groupby('Product')['Quantity'].sum().nlargest(5)
print("\nTop-selling products:")
print(top_products)

# Customer Segmentation
customer_demographics = sales_data.groupby(['Age', 'Gender'])['CustomerID'].nunique()
print("\nCustomer segmentation by age and gender:")
print(customer_demographics)

# Sales Forecasting (Example: Simple moving average)
# Calculate 3-month moving average of sales
sales_data['MovingAvg'] = sales_data['Sales'].rolling(window=3).mean()

# Visualization (Example: Line plot of monthly sales trends)
import matplotlib.pyplot as plt

monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

