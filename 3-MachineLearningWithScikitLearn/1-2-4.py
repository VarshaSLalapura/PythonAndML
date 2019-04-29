import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
import os
import time
from datetime import datetime

path = "/home/varshalalapura/Desktop/datasets/intraQuarter"

def Key_Stats(gather = "Total Debt/Equity (mrq)"):
    stats_path = path + "/_KeyStats"
    print(stats_path)
    # inside the folder is a list of folders of stock
    stock_list = [x[0] for x in os.walk(stats_path)] # x[0] is the start location, the directory _KeyStats
    print(stock_list[0])
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        # print(each_dir)
        # print(type(each_dir))
        ticker = each_dir.split("/")[-1]
        # print(ticker)
        # print(type(ticker))
        # print(each_file)
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                file_full_path = each_dir + '/' + file # step 2
                print(file_full_path) # step 2
                source = open(file_full_path,'r').read() # step 3
                # print(source)
                value = source.split(gather + '</td><td class="yfnc_tabledata1"')[1] # step 4
                print(ticker,value)
                # print(date_stamp,unix_time)


                time.sleep(15)


# this pgm is to load the dataset from sklean,
# normalize the data, apply svm on the data, fit it,
# run the prediction essentially


# it is possible for svm gamma to be selected automatically
# https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html

Key_Stats()

