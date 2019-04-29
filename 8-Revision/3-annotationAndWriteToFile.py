import os
import numpy as np

path = "/home/varsha/Desktop/AnuPriya/DATA_OLD"

dir_name = "1"

train_dir = os.path.join(path, dir_name)
print(train_dir)
print('no. of dirs inside this:', np.size(os.listdir(train_dir)))
sub_dir = [x[0] for x in os.walk(train_dir)]

print('list of sub dirs inside this: ', sub_dir)
print()
i = 1
with open(os.path.join('/home/varsha/Desktop/AnuPriya', 'annotation_train.txt'), 'w') as f:
    for each_sub_dir in sub_dir[1:]:  # if I dint give in braces[1:], it will include the sub-dir itself
        # i.e 0th index is [1,3,4,5,7,6,2]
        second_slash = sub_dir[i].split('/')[-1]
        i += 1
        # print(second_slash)
        each_file = os.listdir(each_sub_dir)
        print(each_file)
        print(len(each_file))
        print()
        new_each_file = [] # [None]*(len(each_file))
        print('length=', len(new_each_file))

        if len(each_file) > 0:
            for file_name in each_file:  # [0:3]
                print()
                print(file_name)  # one element, str, html file
                # print(type(file))
                gt = file_name.split('_')[1]
                print(gt)
                new_file_name = dir_name + '/' + second_slash + '/' + str(file_name) + ' ' + gt
                # i += 1
                print(new_file_name)
                # new_each_file.append(new_file_name)
                f.write('%s\n' %new_file_name)
        # print(new_each_file)





