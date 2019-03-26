# operating on pixels and roi of an image using cv2

import cv2

imloc = r"/home/varshalalapura/Desktop/Inspiration/1.jpg"
img = cv2.imread(imloc, cv2.IMREAD_UNCHANGED)
cv2.imshow('image1', img)


# chose a pixel value:
print(img[30, 40])
img[30, 40] = (255, 255, 255)
print(img[30, 40])

# access a roi :
roi = img[0:30, 0:40]
cv2.imshow('roi', roi)

# access another roi:
roi1 = img[150:300, 200:400]
cv2.imshow('roi1', roi1)

# insert this at the 0,0 position of the image:
img[0:(300-150), 0:(400-200)] = roi1
cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()