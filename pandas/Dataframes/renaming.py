import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

# Check out your DataFrame `df`
print(df)

# Define the new names of columns
newcols = {
    'A': 'new_column_1',
    'B': 'new_column_2',
    'C': 'new_column_3'
}

print("----Rename columns----")
# Use `rename()` to rename columns
print(df.rename(columns=newcols, inplace=True))

print("----Rename index----")
# Rename index
print(df.rename(index={1: 'a'}))
