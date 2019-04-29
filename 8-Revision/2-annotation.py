import os
import numpy as np

path = "/home/varsha/Desktop/AnuPriya/DATA_OLD"
dir_name = "1"

train_dir = os.path.join(path,dir_name)
print(train_dir)
print('no. of dirs inside this:', np.size(os.listdir(train_dir)))
sub_dir = [x[0] for x in os.walk(train_dir)]
print('list of sub dirs inside this: ', sub_dir)
print()
for each_sub_dir in sub_dir[1:2]:  # if I dint give in braces[1:], it will include the sub-dirs list [1,3,4,5,7,6,2]
    each_file = os.listdir(each_sub_dir)
    print(each_file)
    print(len(each_file))
    print()

    if len(each_file) > 0:
        for file_name in each_file[0:3]:  #[0:3]
            print()
            print(file_name) # one element, str, html file
            # print(type(file))
            gt = file_name.split('_')[1]
            print(gt)
            new_file_name = str(file_name) + ' ' + gt
            print(new_file_name)





