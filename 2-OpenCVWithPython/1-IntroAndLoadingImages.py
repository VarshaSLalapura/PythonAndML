import numpy as np
from matplotlib import pyplot as plt
import cv2



# the "OpenCV method"
# image location, read the location- imread(imloc) with params, display using imshow, wait key, close window - destoryAllWindow
imloc = r"/home/varshalalapura/Desktop/Inspiration/1.jpg"
img = cv2.imread(imloc, cv2.IMREAD_GRAYSCALE)
# cv2.IMREAD_COLOUR = 1, cv2.IMREAD_UNCHANGED = -1, cv2.IMREAD_GRAYSCALE = 0
# cv2.imshow('image',img)


# the "matplotlib method"
# error if i wrote : plt.imshow('img', cmap='gray',interpolation='bicubic')

plt.imshow(img,cmap = 'gray', interpolation= 'bicubic') # imshow to display mostly and not plt.plot for the image
plt.plot([50,100],[80,100],'y',linewidth=5) # d diamonds, c continuous red line, b continuous blue line, g - green,
# y - yellow
plt.show()

# for writing the image to the directory
# cv2.imwrite('image_gray',img)
while True:
    if cv2.waitKey(0) & 0xFF == ord('d'):
        break

cv2.destroyAllWindows()