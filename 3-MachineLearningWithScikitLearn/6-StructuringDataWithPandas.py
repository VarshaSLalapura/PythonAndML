import numpy as np
import matplotlib
import sklearn
import os
from datetime import datetime
import time
import pandas as pd

path = "/home/varshalalapura/Desktop/datasets/intraQuarter"
dir_name = "_KeyStats"

def Key_Stats(gather = "Total Debt/Equity (mrq)"): # has put a colon inside mrq as mrq: full code was showing
    # something else

    stats_path = os.path.join(path,dir_name) # had written /_Key_Stats, so dint reach the folder at all
    # print(stats_path) # this is a path
    # we know from outside that this direc has sub directories, r2
    stock_list = [x[0] for x in os.walk(stats_path)]
    # print(stock_list)
    df = []
    for each_dir in stock_list[1:]:
        df = pd.dataframe(['Date', 'UnixTime', 'Ticker', 'DERatio'])
        each_file = os.listdir(each_dir)
        ticker = each_dir.split('/')[-1]
        if len(each_file) > 0:
            for file in each_file:
                file_full_path = os.path.join(each_dir,file)
                # print(file_full_path)
                source = open(file_full_path, 'r').read()
                value = source.split(gather + ':</td><td class="yfnc_tabledata1">')[-1].split('</td>')[0]
                date_stamp = datetime.strptime(file, "%Y%m%d%H%M%S.html")
                unix_time = time.mktime(date_stamp.timetuple())
                df.append({'Date': date_stamp, 'UnixTime': unix_time, 'Ticker': ticker, 'DERatio': value}, ignore_index = True)
                # print(ticker + ':', value)
            time.sleep(15)
            print(df)
Key_Stats()



