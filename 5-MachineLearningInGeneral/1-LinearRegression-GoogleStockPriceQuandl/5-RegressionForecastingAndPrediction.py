import quandl
import pandas as pd
import numpy as np
from sklearn import preprocessing, model_selection, cross_decomposition, svm, linear_model

df = quandl.get('WIKI/GOOGL')
# 1. Get data from quandl
# 2. See the columns and see what you need
# 3. make the df with those cols, caveat [[]]
# 4. display top 6
# 5. meaningful feautres
# 6. label
# 7. fillnan, inplace=True
# 8. meaningful label
# 9. dropna
# 10. preprocessing.scale data
# 11. dropna if any again
# 12. model_selection -> train,test split
# 13. convert to np features and labels
# 14. define the clf
# 15. fit it on the train set
# 16. score the clf on test set
# 17. mark it as confidence / accuracy.
# 18. for loop for all the possible kernels in the svm , linear, poly, rfb, sigmoid

print(df.head())
df = df[["Adj. Close", "Adj. High", "Adj. Low", "Adj. Open", "Adj. Volume"]]
print(df.head())
df["HL_PCT"] = (df["Adj. High"] - df["Adj. Low"]) / df["Adj. Low"]
df["PCT_CHG"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"]
df = df[["Adj. Close", "HL_PCT", "PCT_CHG", "Adj. Volume"]]
print(df.head())

# choose one as a label, related to the price
forecast_col = "Adj. Close"
# print(df.size)
# df.fillna(-9999, inplace=True)
# print(df.size)
forecast_out = int(math.ceil(0.001*len(df))) # with 0.01, we see the label is far from the close, because
# we went more days backward, if we use 0.001, we only go 4 days back and so the close and label value are
# close
# print(forecast_out)
df["label"]= df[forecast_col].shift(-forecast_out) # what is shifted by how much
# also this is automatically added to the df, check the print
print(df.head())

# # print(df.head(10))
# # print(df.tail(10))
# # remove all the nan
df.dropna(inplace=True)
# print(df.size)
# print(df.tail(10))
# separate out the feature and the label

# X = df[["Adj. Close", "HL_PCT", "PCT_CHG", "Adj. Volume"]]
# X1 = df.drop(['label'],1)
X = np.array(df.drop(['label'], 1)) # check df.drop

# print(X.head())
# print(np.size(X))
y = np.array(df["label"])
# print(np.size(y))
X = preprocessing.scale(X)
# after preprocessing also, drop the na values
df.dropna(inplace=True)
# y = np.array(df["label"])
print(len(y),len(X))
# # print(y.head())
# # add preprocessing, cross_validation (cross_decomposition)and svm from sklearn
# # preprocessing.scale()
# #
# #
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)
clf1 = svm.SVR(gamma='auto')
clf1.fit(X_train, y_train)
confidence = clf1.score(X_test, y_test)
print(confidence)
clf2 = linear_model.LinearRegression()
clf2.fit(X_train, y_train)
confidence = clf2.score(X_test, y_test)
print(confidence)

# for k in ['linear','poly','rbf', 'sigmoid']:
#     clf = svm.SVR(kernel=k, gamma=0.01)
#     clf.fit(X_train, y_train)
#     confidence= clf.score(X_test, y_test)
#     print(confidence)