# Regression Introduction:

import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
# this is stock data of Google
# stock at opening of the day, Stock when it was high, Stock when it was low, Stock at close time, Stock volume
print(df.head())
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
# try df["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]
print(df.head())

# Sentdex is picking columns that are meaningful, also seeing how they are related to each other
# because linear regression is not going to seek out how the features are related to each other,
# its only going to work out on the features feed through it

# So he defines the relationship between those features:
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low']
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']
df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]
print(df.head())


