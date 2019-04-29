import pandas as pd
import matplotlib.pyplot as plt
import os

path = "/home/varshalalapura/Desktop/datasets/AvacadoPricing"
file_name = "avocado.csv"

df = pd.read_csv(os.path.join(path, file_name))
print(df.head(5))
albany_df = df[df["region"] == "Albany"]
# note the square braces around inside which we look for the col to be searched
# and the df of that data , df[]

print(albany_df.set_index("Date", inplace=True))
plt.plot(albany_df["AveragePrice"])
albany_df["AveragePrice"].plot()
plt.show()