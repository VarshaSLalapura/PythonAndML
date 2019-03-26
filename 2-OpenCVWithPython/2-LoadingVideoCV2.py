# make the video location object
# read that object

# since it is video , it will be indefinately reading, so
# the while loop with a certain key

import cv2

vidloc = "/home/varshalalapura/Desktop/Inspiration/drop.avi"
cap = cv2.VideoCapture(vidloc)


# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.
# https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
fourcc = cv2.VideoWriter_fourcc(*'XVID') # 2, for writing

out = cv2.VideoWriter('/home/varshalalapura/Desktop/Inspiration/dropSend.avi', fourcc, 100.0, (640, 480)) # 2
# out = cv2.VideoWriter('/home/varshalalapura/Desktop/Inspiration/output.avi',cv2.VideoWriter_fourcc(*'XVID'),
# 20.0, (640,480), isColor=0)
# https://docs.opencv.org/3.0-beta/modules/videoio/doc/reading_and_writing_video.html#videowriter

# while (cap.isOpened()):
while True:

    ret, frame = cap.read()
    colourful = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    # colourful = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(frame)  # 2
    cv2.imshow('drop', frame)
    cv2.imshow('drop_beautiful', colourful)
    # if cv2.waitKey(0) & 0xFF==ord('d'):
    if cv2.waitKey(100) & 0xFF==ord('d'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()

