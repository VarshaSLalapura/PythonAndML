import numpy as np
import matplotlib
import sklearn
import os
from datetime import datetime
import time

path = "/home/varshalalapura/Desktop/datasets/intraQuarter"
dir_name = "_KeyStats"

def Key_Stats(gather = "Total Debt/Equity (mrq)"):

    stats_path = os.path.join(path,dir_name)

    stock_list = [x[0] for x in os.walk(stats_path)]

    for each_dir in stock_list[1:5]:
        # print(each_dir) # this is the full path of each directory
        ticker = each_dir.split('/')[-1]
        # print(ticker) # this is the directory name extracted

        each_file = os.listdir(each_dir)

        # print(each_file) # we can view the files in the directories
        if len(each_file) > 0:
            for file in each_file:

                date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_path_file = each_dir + '/' + file
                source = open(full_path_file,'r').read()
                # print(source)
                value = source.split(gather + ':</td><td class="yfnc_tabledata1">')[-1].split('</td>')[0]

                print(ticker+' :',value)


                # print(date_stamp,unix_time)
            time.sleep(10)







Key_Stats()