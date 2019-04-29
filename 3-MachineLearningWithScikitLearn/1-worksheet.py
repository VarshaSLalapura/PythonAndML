import numpy as np
import matplotlib
import sklearn
import os
import time
from datetime import datetime

path = "/home/varshalalapura/Desktop/datasets/intraQuarter"
# go to the specific directory
stats_path = path + "/_KeyStats"
print('stats_path = ' , stats_path) # object -> path -> means a dir in which you have sub directories, so route 2       object = path(directory), type = str(directory)
print('type(stats_path)= ', type(stats_path)) # type = str
print(np.size(os.listdir(stats_path))) # size = 560
# print('@@ = ',os.listdir(stats_path)) # list of strs -> whats inside r2 -> each str is another file -> route 2

# # route 2
stock_list = [x[0] for x in os.walk(stats_path)]
# print('stock_list = ',stock_list) # list of paths -> mean a list of dirs -> each has html files and not any more directory, so route 1, check the items in the list object = paths(directories), type = list(directory)
# print('type of stock_list = ',type(stock_list)) # 2. this is a list, check items in the list
# print(np.size(stock_list)) # size = 561, 1 is the parent directory itself
# print(stock_list[0])
# print(os.listdir(stock_list[1])) # from 2
#
for each_dir in stock_list[1:]: # because list is returned:  (stock_list[1:],list,directories), each_dir, variable, one_directory -> open the directory
    # print(each_dir) #
    # print(type(each_dir)) #path,str,(directory)
    each_file = os.listdir(each_dir)
    print(each_file) #set of strings,str,(htmlfile)
    # remember not this -> each_file = [y[0] for y in os.walk(each_dir)]
    # print(each_file)
    print(type(each_file)) # list ,,,, list of strings, open the list

    if len(each_file) > 0:
        for file in each_file:
            print(file) # one element, str, html file
            print(type(file))
            date_time = datetime.strptime(file,'%Y%m%d%H%M%S.html')
            unix_time = time.mktime(date_time.timetuple())
            # #unix_time = time.mktime(date_stamp.timetuple())
            print(date_time,unix_time)
            time.sleep(15)



































# iterate the entire directory of stocks as a list named stock_list,
# stock_list = [x[0] for x in os.walk(stats_path)]
# # note the 1st item is the parent directory itself
# print(stock_list[0])
# # check how many sub-directories are there in the current directory
# print(type(stock_list))
# print(np.size(stock_list))
# # iterate over the files in the sub-directory
# print(os.listdir(stock_list[1]))
# print(type(stock_list[1]))

# see whats in the list
# for each_item in stock_list[1:]:
#     print(each_item) # this is a directory
#     print(type(each_item)) # for python it is a str
#     # print(os.listdir(each_item))
#     # print(type(os.listdir(each_item))) # for python this is list
#     each_file = os.listdir(each_item)
#     # if len(each_file) > 0:
#     #     for file in each_file:
#     #         date_time = date.time()

