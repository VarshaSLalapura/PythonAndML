# T4: Image operations using openCV

# load the image and read it

import numpy as np
import cv2

imloc = r"/home/varshalalapura/Desktop/Inspiration/1.jpg"
img = cv2.imread(imloc, cv2.IMREAD_COLOR)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# access a pixel
pxl = img[55,55] # img[x,y]
print(pxl)

# change the pixel value
img[55,55] = (255,255,255)
print(pxl)

#Region of Image, or RoI, or sub-image of an image

roi = img[100:150, 100:150] # img[x1:x2, y1:y2]
print(roi) # this will print truncated values

# change the roi to all white pixels
roi = [255,255,255]
print(roi)

# change the roi in the image as white pxls
img[100:150, 100:150] = (255,255,255)
# display the image
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# slice the image somewhere, roi/sub-image to call it
# put the slice into image like this
# [start_x:x2-x1, start_y:y2-y1] here start_y = 0, x2-x1 = 250-200 , y2-y1 = 450-400, start_y = 0
centre_up = img[200:250,400:450]
img[0:50, 0:50] = centre_up
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() # u ll see roi copied to the top , her hair :)




