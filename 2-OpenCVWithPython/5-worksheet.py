# T5: Image arithmetic and logic using opencv

import cv2

# take two images of the "SAME SIZE"
# and do an imread of the 2 images

img1 = cv2.imread(r"/home/varshalalapura/Desktop/Inspiration/3D-Matplotlib.png")
img2 = cv2.imread(r"/home/varshalalapura/Desktop/Inspiration/mainsvmimage.png")
img3 = cv2.imread(r"/home/varshalalapura/Desktop/Inspiration/mainlogo.png")
cv2.imshow('img3', img3)

row, col, channel = img3.shape
print(row, col, channel)
# 255 - White
# 0 - black
roi = img2[0:row, 0:col]
cv2.imshow('roi', roi)


img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
cv2.imshow('img2gray', img2gray)

ret, mask1 = cv2.threshold(img2gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow('mask1', mask1)
ret, mask = cv2.threshold(img2gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY_INV)
cv2.imshow('mask', mask)
mask_inv = cv2.bitwise_not(mask) # same as mask1
cv2.imshow('mask', mask_inv)

img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('img_bg', img_bg)
img_fg = cv2.bitwise_and(img3, img3, mask=mask)
cv2.imshow('img_fg', img_fg)

dstn = cv2.add(img_fg, img_bg)
img2[0:row, 0:col] = dstn
cv2.imshow('final', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()