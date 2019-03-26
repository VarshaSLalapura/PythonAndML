# fit one image onto another

import cv2
import numpy as np

# note: I have taken mainsvm as img to which logo is to be inserted,
# Sentdex took 3D-Matplotlib which has whiter background to which he inserted the logo,
# so the method is correct , dont match the two results as the inputs are not the same :)

imloc1 = r"/home/varshalalapura/Desktop/Inspiration/mainsvmimage.png"
imloc2 = r"/home/varshalalapura/Desktop/Inspiration/mainlogo.png"
# display img1
img1 = cv2.imread(imloc1)
cv2.imshow('img1', img1)
# display img2
img2 = cv2.imread(imloc2)
cv2.imshow('img2', img2)

# we want to insert the main logo img2 into img1
# for that step 1:
# convert the image to be inserted as gray scale

img2_grayScale = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) # not cv2.IMREAD_GRAYSCALE,
# because this is not reading the image as GRAY, its converting the image to GRAY
cv2.imshow('img1_grayScale', img2_grayScale)

# find the roi where the second image has to be inserted
# the roi should be of the size of the second image to be inserted
# so find its shape
row,col,channel = np.shape(img2)
print(row,col,channel) # give 250,500,4? 4? find out BGRA
# the roi will be this in img1
roi = img1[0:row, 0:col]
cv2.imshow('roi', roi)

# # take img2, grayed out and make two masks
# ret1, mask1 = cv2.threshold(img2_grayScale, thresh=220, maxval=255, type = cv2.THRESH_BINARY_INV)
# cv2.imshow('mask1', mask1)
#
# mask2 = cv2.bitwise_not(mask1)
# cv2.imshow('mask2',mask2)
#
# # we want foreground of logo(img2) to be allowed
# img_fg = cv2.bitwise_and(img2,img2,mask=mask1)
# cv2.imshow('img_fg', img_fg)
# img_bg = cv2.bitwise_and(roi,roi,mask=mask2)
# cv2.imshow('img_bg', img_bg)
#
# dst = cv2.add(img_bg,img_fg)
# img1[0:row,0:col] = dst
#
# cv2.imshow('final', img1)















cv2.waitKey(0)
cv2.destroyAllWindows()

