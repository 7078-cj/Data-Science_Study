import pandas as pd
import os

base = os.path.dirname(__file__)
file_path = os.path.join(base, "orders.csv")
df = pd.read_csv(file_path)

#filter the products that has Electronics categ
print(df[df["Category"] == "Electronics"])

#with country USA
print(df[(df["Category"] == "Electronics") & (df["Country"] == "USA")] )

#get a data that has quantity greater than 20
print( df[ df["Quantity"] > 20 ] )

#get data with customer name startswith A
print( df[df["CustomerName"].str.startswith("A")] )

#get data if its in USA, Sweden, Brazil
print( df[df["Country"].isin(["USA", "Sweden", "Brazil"]) ] )