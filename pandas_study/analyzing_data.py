import pandas as pd
import os

base = os.path.dirname(__file__)
file_path = os.path.join(base, "orders.csv")
df = pd.read_csv(file_path)

#it show the count of how many with the attribute
print(df["Country"].value_counts())

#it will show the sum of the products grouped by country
print(df.groupby("Country")["Price"].sum())

#saving the edited csv
df.to_csv("order_1", index=False)