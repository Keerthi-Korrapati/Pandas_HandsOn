import pandas as pd
import numpy as np

print("----Replacing occurrences----")
df = pd.DataFrame({"Student1":['OK','Awful','Acceptable'],
                   "Student2":['Perfect','Awful','OK'],
                   "Student3":['Acceptable','Perfect','Poor']})
print(df)
# Replace the strings by numerical values (0-4)
print(df.replace(['Awful', 'Poor', 'OK', 'Acceptable', 'Perfect'], [0, 1, 2, 3, 4]))

print("----Regex Replacing----")
df1 =  pd.DataFrame([["1\n", 2, "3\n"], [4, 5, "6\n"] ,[7, "8\n", 9]])
print(df1)
# Replace strings by others with `regex`
print(df1.replace({'\n': ''}, regex=True))

print("----Removing parts----")
df2 = pd.DataFrame([["+-1aAbBcC", "2", "+-3aAbBcC"], ["4", "5", "+-6aAbBcC"] ,["7", "+-8aAbBcC", "9"]])
print(df2)
# Delete unwanted parts from the strings in the first column
df2[0] = df2[0].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))
print(df2)


print("----Splitting Text----")
df3 = pd.DataFrame({"Age": [34, 22, 19],
                   "PlusOne": [0, 0, 1],
                   "Ticket": ["23:44:55", "66:77:88", "43:68:05 56:34:12"]})
print(df3)
# Split out the two values in the third row
# Make it a Series
# Stack the values
ticket_series = df3['Ticket'].str.split(' ').apply(pd.Series, 1).stack()
# Get rid of the stack:
# Drop the level to line up with the DataFrame
ticket_series.index = ticket_series.index.droplevel(-1)
print(ticket_series)
print(df3)

print("----Functions----")
doubler = lambda x: x*2
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])
print(df)

# Apply the `doubler` function to the `A` DataFrame column
df['A'].apply(doubler)
