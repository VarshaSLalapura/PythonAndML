# this is about nested lists, traversing directory of a directory of a directory to reach the one string at the end

import numpy as np
import sklearn
import os
from datetime import datetime
import time

path = "/home/varshalalapura/Desktop/datasets/intraQuarter"


def Key_Stats(gather = "Total Debt/Equity (mrq)"):
    print('function starts....')
    stats_path = path + '/_KeyStats'
    # print(stats_path) # path (/home/varshalalapura/Desktop/datasets/intraQuarter/_KeyStats)
    # print(type(stats_path)) #str
    # holds many directories inside
    # to open the directories along the path and convert to a list
    stock_list = [x[0] for x in os.walk(stats_path)]
    # print(stock_list) # list of paths
    # print(type(stock_list)) # list
    # holdes html files inside
    # open it up
    for each_dir in stock_list[1:]: # list(each_dir) of list(stock_list)
        # print(each_dir) # each item in the list, or each directory in the list of stock
        # print(type(each_dir)) # str
        # print(stock_list[1:]) # list of paths
        # print(type(stock_list[1:])) # list
        # open the list within
        each_file = os.listdir(each_dir) # list(each_file) of list(each_dir)
        # print(each_file) # html files in each directory
        # print(type(each_file)) # list of words ([20051216053323.html,....])
        # each of it is a list,
        # open the list
        if len(each_file) > 0:
            for file in each_file:
                # print(each_file) # list of html files of the loops(each_dir)
                # print(type(each_file)) # list
                # print(file) # one file in the each_file list
                # print(type(file)) # str (20060316131810.html)
                # reached the end of the directory-file structure
                date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                print(date_stamp , unix_time)
                time.sleep(10)


Key_Stats()

























# print(os.path.join(path,'/_KeyStats'))