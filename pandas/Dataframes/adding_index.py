import pandas as pd
import numpy as np

'''df = pd.DataFrame({"A": [1, 4, 7], "B": [2, 5, 8], "C": [3, 6, 9]})
print(df)

print("----Set 'C' as the index----")
df.set_index('C')'''

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index= [2, 'A', 4], columns=[48, 49, 50])

# Pass `2` to `loc`
print(df.loc[2])

# Pass `2` to `iloc`
print(df.iloc[2])

print("----Adding index----")
df1 = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index= [2.5, 12.6, 4.8], columns=[48, 49, 50])

df1.loc[2] = [11, 12, 13] # This will make an index labeled `2` and add the new values
print(df1)

print("----Adding column----")
df2 = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])
df2['D'] = df2.index
print(df2)
# Append a column to `df` another method
print("----another method----")
df2.loc[:, 4] = pd.Series(['5', '6', '7'], index=df2.index)
print(df2)
print("----Reset index----")
df_reset = df2.reset_index(level=0, drop=True)
print(df_reset)