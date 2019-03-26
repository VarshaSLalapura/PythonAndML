# Handling non-numeric data in pandas
# titanic dataset

import pandas as pd
import os
import numpy as np
pd.set_option('display.max_columns', 15)

path = "/home/varshalalapura/Desktop/datasets/Titanic"
filename = "titanic3rows.xls"

my_file = os.path.join(path, filename)
# print(my_file)

df = pd.read_excel(my_file)
# print(df.head())

df.drop(['body', 'name'], 1, inplace=True)
# print(df.head())
df.dropna(0, inplace=True)
# print(df.head())

# convert to np array
# converting non-numeric data


def convert_non_numeric(daf):

    # pd.convert_objects(convert_numeric=True)
    df_columns_indices = df.columns
    # print(df_columns_indices)
    df_columns = df.columns.values
    # print(df_columns)

    # define a dic that holds text:int pairs
    txt_int_dict = {}

    def txt_to_int(txt):
        return txt_int_dict[txt]

    columns = ['pclass', 'survived', 'sex', 'age',]  # 'sibsp', 'parch', 'ticket']

    for column in columns:
        # print(column)
        # print(df[column], type(df[column]))

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_list = df[column].values.tolist()  # error, df[columns].values
            print(column_list)
            unique_elements = set(column_list)  # this is a dict
            # print(unique_elements)
            x = 0
            for elems in unique_elements:
                if elems not in txt_int_dict:
                    # print(elems)
                    txt_int_dict[elems] = x
                    x += 1
            print(txt_int_dict)
            print(df[column])

            df[column] = list(map(txt_to_int, df[column]))
            print((df[column]))


#  # columns = ['pclass', 'sex', 'cabin']
#     for column in columns:  # for eac column in the df
#         if df[column].dtype != np.int64 and df[column].dtype != np.float64:  # if it is non-numeric
#             # convert to a list
#             column_list = df[column].values.tolist()
#             # find the unique elements
#             unique_elements = set(column_list)
#             # not iterate over the unique elements and put to the dict with value starting from 0
#             x = 0
#             for unique in unique_elements:
#                 if unique not in txt_to_int_dict:
#                     txt_to_int_dict[unique] = x
#                     x += 1
#
#             print('txt_to_int_dict', txt_to_int_dict)
#
#             df[column] = list(map(convert_txt_int, df[column]))
#             print(df[column])
#     return df
#
#
# handle_non_numeric_data(daf=df)
# print(df.head())
#




convert_non_numeric(daf=df)

# df = np.array(df, dtype=np.float64)
# print(df)
