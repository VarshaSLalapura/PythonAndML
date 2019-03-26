# This work sheet is to draw lines, circles, rectangles and polygons on images using openCV

import cv2
import numpy as np


imloc = r"/home/varshalalapura/Desktop/Inspiration/3.jpg"
img = cv2.imread(imloc, cv2.IMREAD_UNCHANGED)


# draw a line on the image
cv2.line(img, (200,400), (300,80), color=(0,255,255), thickness=5) # for matplotlib, ([][])

# draw a circle:
cv2.circle(img, center=(150,150), radius=50, color=(255,0,0), thickness=6) # image starts from l2ft top as (0,0)

# draw a rectangle:
cv2.rectangle(img, (200, 200), (400, 500), color=(255,255,0), thickness=7)

# draw a polygon:
points = [[50,50],[200,200],[450,450],[300,300],[150,150]]
pts = np.array(points, dtype=np.int32)
print(pts)
cv2.polylines(img, [pts], isClosed=1, color=(255,255,255), thickness=8)

# write some text inside:
text1 = "Work but cheerful and loving it"
cv2.putText(img, text1, org=(30,30), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)



# display:
cv2.imshow('image3',img)
cv2.waitKey(0)
cv2.destroyAllWindows()