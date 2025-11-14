import pandas as pd
import os

base = os.path.dirname(__file__)
file_path = os.path.join(base, "orders.csv")
df = pd.read_csv(file_path)


#it will drop tables with null values
df.dropna()

#it will fill with data if it has null
df.fillna({"OrderID": 0}, inplace=True)

#renaming columns
df.rename(columns={"OrderID": "Order ID"}, inplace=True)