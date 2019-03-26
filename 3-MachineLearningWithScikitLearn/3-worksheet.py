import numpy as np
import matplotlib
import sklearn
import os
from datetime import datetime
import time

path = "/home/varshalalapura/Desktop/datasets/intraQuarter"


def Key_Stats(gather = "Total Debt/Equity (mrq)"):

    stats_path = path + '/_KeyStats' # had written /_Key_Stats, so dint reach the folder at all
    # print(stats_path) # this is a path
    # we know from outside that this direc has sub directories, r2
    stock_list = [x[0] for x in os.walk(stats_path)]
    # print(stock_list)
    for each_dir in stock_list[1:5]:
        # print(each_dir) # this is the full path of each directory
        ticker = each_dir.split('/')[-1]
        # print(ticker) # this is the directory name extracted
        # we know from outside that each_dir contains set of html "files", r1
        each_file = os.listdir(each_dir) # dont do a for loop here, because we are goin to one file of a directory
        # and extracting it one at a time
        # print(each_file) # we can view the files in the directories
        if len(each_file) > 0:
            for file in each_file:
                # print(file) # final string
                # print(each_file) # list of html files
                date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_path_file = each_dir + '/' + file
                source = open(full_path_file,'r').read()
                # print(source)
                value = source.split(gather + ':</td><td class="yfnc_tabledata1">')[-1].split('</td>')[0]
                # value = source.split(gather +' :</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                # had missed the colon, really careful to split the file, need to understand this
                print(ticker+':',value)

                # print(date_stamp,unix_time)
            time.sleep(10)







Key_Stats()