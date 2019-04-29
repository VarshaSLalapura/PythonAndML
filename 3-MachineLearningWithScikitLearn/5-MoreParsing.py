# this code is to parse the html file and look for the value of Debt Equity Ratio(DE ratio)




import os
from datetime import datetime
import time

path = "/home/varshalalapura/Desktop/datasets/intraQuarter"
dir_name = "_KeyStats"


def Key_Stats(gather = "Total Debt/Equity (mrq)"): # what you are searching for should be exactly matching the string in
    # the html file
    dir = os.path.join(path,dir_name)
    # print(dir)
    stock_list = [x[0] for x in os.walk(dir)] # this will include the parent directory, so exclude it while opening it
    # print(stock_list)
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split('/')[-1]
        # print(ticker)
        if len(each_file)>0:
            for file in each_file:
                # print(file)
                file_full_path = each_dir + '/' + file
                # print(file_full_path)
                # read the file names in a format
                # with open(file_full_path,'r') as f:
                    # f.read()
                source = open(file_full_path, 'r').read()
                value = source.split(gather + ':</td><td class="yfnc_tabledata1">')[-1].split('</td>')[0]
                # value = source.split(gather + ':</td><td class="yfnc_tabledata1">')[-1].split('</td>')[0]

                # value = f.split(gather + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                # date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                # unix_time = time.mktime(date_stamp.timetuple())
                print('@@@@',ticker+ ':', value)
                #     # print(date_stamp,unix_time)
                # # parse the file for the value
            time.sleep(10)

        # if len(each_file) > 0:
        #     for file in each_file:
        #         # print(file) # final string
        #         # print(each_file) # list of html files
        #         # date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
        #         # unix_time = time.mktime(date_stamp.timetuple())
        #         full_path_file = each_dir + '/' + file
        #         source = open(full_path_file,'r').read()
        #         # print(source)
        #         value = source.split(gather + ':</td><td class="yfnc_tabledata1">')[-1].split('</td>')[0]
        #         # value = source.split(gather +' :</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        #         # had missed the colon, really careful to split the file, need to understand this
        #         print(ticker+':',value)
        #
        #         # print(date_stamp,unix_time)
        #     time.sleep(10)







Key_Stats()


