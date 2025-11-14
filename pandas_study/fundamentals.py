import pandas as pd
import os

base = os.path.dirname(__file__)
file_path = os.path.join(base, "orders.csv")
df = pd.read_csv(file_path)
# print(df)

# print(df.head())
#show the first 5 data of the df

# print(df.tail())
#shows last 5

# print(df.info())
#show the info about every data in df

print(df.describe())
#this generates descriptive statistics

print(df.index)
#RangeIndex(start=0, stop=40, step=1) show the index size of the df