# 5-worksheet.py - RegressionForcastingAndPrediction.py
import quandl
import numpy as np
import math
from sklearn import preprocessing, model_selection, svm, linear_model
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

df = quandl.get('WIKI/GOOGL') # get the ticker from quandl
# print(df.head())
df = df[["Adj. Close", "Adj. High", "Adj. Low", "Adj. Open", "Adj. Volume"]]
# print(df.head())
df["HL_PCT"] = (df["Adj. High"] - df["Adj. Low"]) / df["Adj. Low"]
df["PCT_CNG"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"]
df = df[["Adj. Close", "HL_PCT", "PCT_CNG", "Adj. Volume"]]
# print(df.head())

forecast_col = "Adj. Close"
df.fillna(-9999, inplace=True)
forecast_out = int(math.ceil(0.001*len(df))) # index till where you want to predict , say 100 values from there
# print(forecast_out)
df["label"] = df[forecast_col].shift(-forecast_out)
# print(df.head())

# print(df.head(10)) # this order of sequence is so crucial
X = np.array(df.drop(["label"], 1))
X = preprocessing.scale(X)
# careful of the order of X_lately and X, if interchanged, logically it is incorrect
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
# df.dropna(inplace=True) # this line or y = y[:-forecast_out]
y = np.array(df["label"])
y = y[:-forecast_out]
print(len(X), len(y))
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

clf = linear_model.LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)
print(forecast_set, confidence, forecast_out)

# now, practise this many times
df["Forecast"] = np.nan

last_date = df.iloc[-1].name  # name here is  the name of the index of the last row
# print(last_date)
last_unix = last_date.timestamp()  # take the date and make it timestamp
print(last_unix)
one_day = 86400
next_unix = one_day + last_unix
print(next_unix)


for i in forecast_set:
    next_date = datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


# for k in ["poly", "linear", "sigmoid", "rbf"]:
#     clf = svm.SVR(kernel = k, gamma=0.001)
#     clf.fit(X_train,y_train)
#     confidence= clf.score(X_test, y_test)
#     print(confidence)

