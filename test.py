import pandas as pd
import numpy as np
from data_cleaning import read_file, change_to_nan
from visualization import extract_columns

# result = read_file(input('give a file name You want to read\n'))
# data = read_csv_file('IRIS.csv')
# array = data.values
# columns = data.columns
# for i in range(len(columns)):
#     columns[i] = data[f'{columns[i]}']

df = pd.DataFrame(
    np.random.randn(5, 3),
    index=["a", "c", "e", "f", "h"],
    columns=["one", "two", "three"],
)
df["four"] = "Bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
df3 = df2.drop(index=['b','g'])
df3.iloc[0, 2] = 'Null'
df3.iloc[4, 1] = 'NA'
df3.iloc[5, 4] = 'NA'
df4 = df3.copy()
Nan_data = change_to_nan(df4, ['slowo', 'one'])
print(df3)
print('\n\n')
print(Nan_data)
