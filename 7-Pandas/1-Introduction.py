# pandas is for analysis of row col type of data
# excel, JSON,SQL,Google BigQuery

import pandas as pd
import matplotlib.pyplot as plt
import os

path = "/home/varshalalapura/Desktop/datasets/AvacadoPricing"
file_name = "avocado.csv"

# read_csv the file
df = pd.read_csv(os.path.join(path,file_name))
print(df)
# top two rows
print(df.head(2))
# last five cols
print(df.tail(5))
# for a particular col
print(df["AveragePrice"])
print(df["AveragePrice"].head())
# for a particular type in a specific col
albany_df= df[df["region"] == 'Albany']
print(albany_df.head())
# if we see the index, first col, nothing meaningful
df = df.set_index("Date")
print(df)
# now print albany_df
print(albany_df)
# this still has the meaningless index
# so note how the pd is returning
# R2:

# albany_df.set_index("Date", inplace = True)
# print(albany_df)
# R1:
# albany_df = albany_df.set_index("Date")
# print(albany_df)