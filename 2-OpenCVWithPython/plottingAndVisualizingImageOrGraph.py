import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# show the location of the image
# read that location
# display the read object

imloc = r"/home/varshalalapura/Desktop/Inspiration/150906-Juan-Jose-Mendez-Fernandez-1.jpg"
img = cv2.imread(imloc, cv2.IMREAD_ANYCOLOR)
# cv2.imshow('beautiful image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# this is using opencv
# now let us try matplotlib
plt.imshow(img)


# drawing line onto the image
plt.plot([50,80],[50,80],'c', linewidth=5)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([10,200,3], [10,400,9], 'rs',  label='line 2')
plt.show()

#more https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

#plot(x, y, color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)


# finally, writing the image to a location
cv2.imwrite(os.path.join("/home/varshalalapura/Desktop/Inspiration/", 'beautiful.jpg'), img)
cv2.waitKey(0)