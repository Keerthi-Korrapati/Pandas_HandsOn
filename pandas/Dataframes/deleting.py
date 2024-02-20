import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]),
                  index=[2.5, 12.6, 4.8, 4.8, 2.5],
                  columns=[48, 49, 50])
print(df)
print("----Delete index----")
print(df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index'))

print("----Drop the column----")
df1 = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

print(df1)
# Drop the column with label 'A'
print(df1.drop('A', axis=1, inplace=True))
# Drop the column at position 1
print(df1.drop(df1.columns[[1]], axis=1))
print(df1)

print("----Deleting duplicate rows----")
df2 = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]),
                  index= [2.5, 12.6, 4.8, 4.8, 2.5],
                  columns=[48, 49, 50])
print(df2)
# Drop the duplicates in `df2`
print(df2.drop_duplicates([48], keep='last'))

print("----Drop the index at position 1----")
print(df2)
print(df2.drop(df2.index[1]))
