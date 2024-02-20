import pandas as pd
import numpy as np


my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print("----2D array as input----")
print(pd.DataFrame(my_2darray))


my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print("----dictionary as input----")
print(pd.DataFrame(my_dict))


my_df = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
print("----DataFrame as input----")
print(pd.DataFrame(my_df))


my_series = pd.Series({"Belgium" : "Brussels", "India" : "New Delhi", "United Kingdom" : "London", "United States" : "Washington"})
print("----Series as input----")
print(pd.DataFrame(my_series))


df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print("----shape property----")
print(df.shape)

print("----len property----")
print(len(df))

