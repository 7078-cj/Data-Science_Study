import pandas as pd
import os

base = os.path.dirname(__file__)
file_path = os.path.join(base, "orders.csv")
df = pd.read_csv(file_path)

print(df["Country"])
#it gets the data with countries

print([df[["Country","Product"]]])
#it gets the countries with the associative product

print(df.iloc[0])
#it return the details of the data with the index 0

print(df.iloc[0]["Shipped"])
#Yes

