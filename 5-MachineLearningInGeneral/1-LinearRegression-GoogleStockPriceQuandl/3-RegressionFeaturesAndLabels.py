# RegressionFeaturesAndLabels.py
# Regression Introduction:

import quandl
import math

df = quandl.get('WIKI/GOOGL')
# this is stock data of Google
# stock at opening of the day, Stock when it was high, Stock when it was low, Stock at close time, Stock volume
print(df.head())
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]] # two braces
# try df["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]
print(df.head())

# Sentdex is picking columns that are meaningful, also seeing how they are related to each other
# because linear regression is not going to seek out how the features are related to each other,
# its only going to work out on the features feed through it

# So he defines the relationship between those features:
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low']
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']
df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]] # two braces, otherwise it is a seq and not a dataframe
print(df.head())
print('type:', type(df))  # class : pandas.core.frame.dataframe

# Q : Can Adj. Close be a feature or a label to think through
# PCT_change and HL_PCT cannot be calculated without the ADJ. Close value,
# so we cant keep it as a label , it would be a biased classifier
# may be last 10 days of Adj. Close to predict the future close is considerable

# some prediction in the future of "price" relating to the col. Adj close,
# may be one day later, week later
# so we need new information to get information out into the future

# we fut a forecast_col as the label and choice Adj close for this set up, later if the context change,
# we can send the label into the object "forecast_col"
forecast_col = "Adj. Close"
# it is a regression problem trying to forsee the price in the future based on these hand made features from the cols of
# of original dataframe
# we remove all the Nan not a number data
df.fillna(-99999, inplace=True)  # see pandas T2 text based explanation to see inplace meaning, connected to returning
# back the df

print('len: ', len(df))  # no. of rows in the df
print(df)  # no. of rows to cols of the df

# using ten days of data to predict today's
forecast_out = int(math.ceil(0.001*len(df)))  # forecast out is 10% of the dataframe in the last ten days may be
print(forecast_out)
# 0.1 is 10 % may be to predict the next ten days, if 0.01% may be predict the next days value
print('df[forecast_col]: ', type(df[forecast_col]))  # class : pandas.core.series.Series
df['label'] = df[forecast_col].shift(-forecast_out)  # and not df["label"] , Sentdex comment is
print("df['label']: ", df['label'])
# # In this case, we're shifting the columns "up" by the forecast_out int amount.
# very important, mistake or error
# if i wrote df['label'] = df["forecast_col"].shift(-forecast_out), it return an error i cant make out
print(df['Adj. Close'].head(10))
print(df.head(10))
print("-----------------------@@@-------------------------------------")
print(df.tail(10))

print('############################################################')
df.dropna(inplace=True)
print(df.head(10))
print("-----------------------####-------------------------------------")
print(df.tail(10))
