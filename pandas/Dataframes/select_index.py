import pandas as pd

df = pd.DataFrame({"A": [1, 4, 7], "B": [2, 5, 8], "C": [3, 6, 9]})
print("----Data----")
print(df)

print("----Using iloc[]----")
print(df.iloc[0][0])

print("----Using loc[]----")
print(df.loc[0]['A'])

print("----Using at[]----")
print(df.at[0,'A'])

print("----Using iat[]----")
print(df.iat[0, 0])

print("----Use `iloc[]` to select row `0`----")
print(df.iloc[0])

print("----Use `loc[]` to select column `'A'`----")
print(df.loc[:, 'A'])
