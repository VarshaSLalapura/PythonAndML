# 2-worksheet- Clustering
# to handle non-numeric data, to assign values to them as a list amd map them correspondingly

import pandas as pd
import numpy as np
from matplotlib import style
import os
pd.set_option('display.max_columns', 15)


style.use('ggplot')

path = "/home/varshalalapura/Desktop/datasets/Titanic"
filename = "titanic.xls"

my_file = os.path.join(path, filename)
print(my_file)

df = pd.read_excel(my_file)
# print(df.shape)
df.drop(['body', 'name'], 1, inplace=True)
df.dropna(0, inplace=True)
# df.convert_objects(convert_numeric=True)
# print(df.shape)
print(df.head())


def handle_non_numeric_data(df):

    # columns = df.columns.values
    # print(columns)
    text_int_dict = {}

    def convert_text_int(text):
        return text_int_dict[text]

    columns = ['pclass', 'survived', 'sex', 'age', 'home.dest']  # see the commas, if not, cant make out error

    for column in columns:
        if df[column].dtype != np.float64 and df[column].dtype != np.int64:  # careful
            # convert the column to a list
            column_list = list(df[column])
            # print(column_list)
            # convert the list to unique_elements list
            unique_elements = set(column_list)
            print(unique_elements)
            x = 0
            for unique_ele in unique_elements:
                if unique_ele not in text_int_dict:
                    text_int_dict[unique_ele] = x
                    x += 1
            # print(text_int_dict)

            df[column] = list(map(convert_text_int, df[column]))  # careful with this line
            print(df[column])
    return df


handle_non_numeric_data(df)
df.head()


