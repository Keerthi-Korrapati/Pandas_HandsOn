import pandas as pd
import matplotlib.pyplot as plt

# Read data from a CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Group by a categorical variable and calculate mean
print("\nMean value by category:")
print(df.groupby('Category')['Value'].mean())

# Plot a histogram of the 'Value' column
plt.hist(df['Value'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
