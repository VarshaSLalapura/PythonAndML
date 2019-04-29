import cv2
import numpy as np
from matplotlib import pyplot as plt

imloc = "/home/varshalalapura/Desktop/Inspiration/mainlogo.png"

img = cv2.imread(imloc, cv2.IMREAD_COLOR)
# display using cv2
# cv2.imshow('image', img)
# cv2.waitKey(1000) # this will open for 1 sec = 1000 millisec, 10,000 => 10 secs
# cv2.destroyAllWindows()

# display using matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.show()
# draw a line may be:
plt.plot([50,80],[100,100],'g',linewidth=5)
plt.show()


# img = cv2.imread(imloc, cv2.IMREAD_UNCHANGED) # cv2.IMREAD_UNCHANGED = -1
#
# # display using cv2
# # cv2.imshow('1_python_logo',img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# # display using matplotlib
# plt.imshow(img,cmap=None,interpolation='bicubic') # this gray is changing the color of the orig logo
# plt.plot([50,80],[100,100],'g', linewidth=5) # first braces are x coords, second braces are y coords
# plt.show()
#
# # plt.imshow(img,cmap = 'gray', interpolation= 'bicubic') # imshow to display mostly and not plt.plot for the image
# # plt.plot([50,100],[80,100],'y',linewidth=5) # d diamonds, c continuous red line, b continuous blue line, g - green,
# # # y - yellow
# # plt.show()
#
# cv2.waitKey(0) # q will break the loop,s to save the image, '0' is parameter -> display indefinitely
# cv2.destroyAllWindows()



# add a line to the plot