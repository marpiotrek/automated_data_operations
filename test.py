import pandas as pd
import numpy as np
from data_cleaning import change_to_nan
from user_communication import FileToDataFrame
from visualization import extract_columns
from information import DataInformation

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
df4 = change_to_nan(df4)
print(df4)
stats = DataInformation(df4)
stats.missing_values()

