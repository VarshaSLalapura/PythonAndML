# Line on an image:

import numpy as np
import cv2

# location
imloc = r"/home/varshalalapura/Desktop/Inspiration/3.jpg"
# read that location
img = cv2.imread(imloc)

# draw the yellow line
cv2.line(img, (0, 0), (150, 150), thickness=15, color=(0, 255, 255))

# draw a rectangle
cv2.rectangle(img, (0,0),(150,150),(255,255,0),15)

# draw a circle
cv2.circle(img, (100, 100), 50, (0, 0, 255), -1) # -1 to fill

# draw a polygon
# points in np.array -> poly
pts = np.array([[10, 5], [20, 30], [42, 53], [60, 80], [80, 120]], np.int32) # note np.int32
# pts = np.reshape((-1, 1, 2))
cv2.polylines(img, [pts], isClosed=True, color=(0,255,0), thickness=1)

# writing text in the image
text = 'This is fun!'
cv2.putText(img, text,(130, 130), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale= 2, color=(255, 0, 0), thickness=5,
            lineType=cv2.LINE_8)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()






