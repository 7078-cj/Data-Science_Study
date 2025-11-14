import pandas as pd
import os

base = os.path.dirname(__file__)
file_path = os.path.join(base, "orders.csv")
df = pd.read_csv(file_path)

#to locate with column
print(df.loc[df["CustomerName"] == "Anna Ivanova"])

#to update
df.loc[df["CustomerName"] == "Anna Ivanova", "Product"] = "CJ"
print(df.loc[df["CustomerName"] == "Anna Ivanova"])

#update to uppercase all country
df["Country"] = df["Country"].str.upper()
print(df["Country"])