# T5: Image arithmetic and logic using opencv

import numpy as np
import cv2

# take two images of the "SAME SIZE"
# and do an imread of the 2 images

img1 = cv2.imread(r"/home/varshalalapura/Desktop/Inspiration/3D-Matplotlib.png")
img2 = cv2.imread(r"/home/varshalalapura/Desktop/Inspiration/mainsvmimage.png")
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)

# simply add the two images
img = img1 + img2

# add them using cv2.add method
img_add_cv2 = cv2.add(img1,img2)

# using addWeighted method
# For the addWeighted method, the parameters are the first image, the weight,
# the second image, that weight, and then finally gamma, which is a measurement of light
img_addWeighted_cv2 = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# try -255, 0 , 100, 255 for the last param(black,bit lighter, light, towards white, white)

# cv2.imshow('added_image',img)
# cv2.imshow('added_using_add_method', img_add_cv2)
# cv2.imshow('added_with_addWeighted_method', img_addWeighted_cv2)

img3 = cv2.imread(r"/home/varshalalapura/Desktop/Inspiration/mainlogo.png")

row,col,channel = img3.shape
print(row,col,channel)
# define the region of image on image 1
roi = img1[0:row,0:col]
cv2.imshow('roi', roi)

# # convert the image to grayscale
# # A grayscale (or graylevel) image is simply one in which the only colors are shades of gray. The reason for
# # differentiating such images from any other sort of color image is that less information needs to be provided for
# # each pixel. In fact a `gray' color is one in which the red, green and blue components all have equal intensity
# # in RGB space, and so it is only necessary to specify a single intensity value for each pixel, as opposed to
# # the three intensities needed to specify each pixel in a full color image.
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#
#
# # threshold it, val > 220, val = 255, else val = 0
# ret, mask = cv2.threshold(img2gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY_INV)
# # cv.THRESH_BINARY_INV : https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
# # cv2.imshow('mask',mask)
# # bit_wise not the mask or thrhold value
# mask_inv = cv2.bitwise_not(mask)
# # cv2.imshow('mask_inv',mask_inv)
#
# # img_bg: and the roi and roi
# # img_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
# # img_fg = cv2.bitwise_and(img2,im2,mask=mask)
#
# # Now black-out the area of logo in ROI
#
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# cv2.imshow('img_bg',img1_bg)
# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# cv2.imshow('img_fg',img2_fg)
#
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:row, 0:col ] = dst
# cv2.imshow('final',img1)

# cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



