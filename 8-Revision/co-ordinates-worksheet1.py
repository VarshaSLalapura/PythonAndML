import os
from PIL import Image

# gt of test set of 14 images
gt_path = "/home/varsha/Desktop/April2019/git-projects/pixel_link/datasetFromICDAR2015/testing/ch4_test_GT_14"

# def get_cords(path):
gt_cords = [None]*(len(os.listdir(gt_path))+1)
for fn in os.listdir(gt_path):
    # print(fn)
    # print(int(fn[7:(len(fn) - 4)]), fn)
    f = open(os.path.join(gt_path, fn))
    lines = f.readlines()
    # print(cords)

    lines_list = [x.rstrip() for x in lines]
    # print(cords)
    # print(type(cords))
    for elem in lines_list:
        # print(elem)
        cords = [int(s) for s in elem.split(',') if s.isdigit()]
        # print(cords)
        x = (cords[6], cords[7])
        # print(x)
        y = (cords[2], cords[3])
        # print(y)
        # gt_cords[int(fn[7:(len(fn) - 4)])] = os.path.join(gt_path, fn)
        area (cords[6], cords[7], cords[2], cords[3])
        print(area)


# test_img_path = "/home/varsha/Desktop/April2019/git-projects/pixel_link/datasetFromICDAR2015/testing/ch4_test_14"
# images = [None]*(len(os.listdir(test_img_path))+1)
# for fn in os.listdir(test_img_path):
#     # img_1.jpg
#     print(fn)
#     print(int(fn[4:(len(fn)-4)]), fn)
#     images[int(fn[4:(len(fn)-4)])] = os.path.join(test_img_path, fn)
#
# print(images)


