# gt file consists of lines(rows) and each line having co-ordinates separated by commas

# we want to read the file and store the lines as pairs of two, tuple of a tuple

path_gt = "/home/varshalalapura/Desktop/git-prjoects/pixel_link/test_data/Challenge4_Test_Task1_GT_ten"
import os
for gt_files in os.listdir(path_gt):
    print(gt_files)


