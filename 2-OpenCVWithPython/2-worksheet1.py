# T1 and T2:
# T1: imloc -> read -> display -> interrupt -> close

# video loc -> VideoCapture - > while in the loop -> read frame -> waitKey -> break -> release -> destroy all windows

import cv2

# video_loc = "/home/varshalalapura/Desktop/Inspiration/drop.avi"
# cap = cv2.VideoCapture(video_loc)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(video_loc,fourcc,20,(620,480))
#
# while True:
#
#       ret,frame = cap.read()
#       p = out.write(frame)
#       cv2.imshow('drop',frame)
#       # cv2.imshow('wrote_drop.avi',p)
#       if cv2.waitKey(30) & 0xFF == ord('q'):
#             break
#
# cap.release()
# out.release()

# imloc = r"/home/varshalalapura/Desktop/Inspiration/3.jpg"
# image = cv2.imread(imloc)
# cv2.imshow('name',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# T2: vidloc -> capture-> loop -> read -> display -> exit loop condition -> release -> close

# vidloc = "/home/varshalalapura/Desktop/Inspiration/drop.avi"
# cap = cv2.VideoCapture(vidloc)
#
# while True:
#     ret, frame = cap.read()
#
#     cv2.imshow('drop',frame)
#     if cv2.waitKey(0) & 0xFF == ord('d'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# T3: vidloc -> capture -> fourcc codec -> loop -> read the capture -> modify -> display 1 and 2 -> write 2 to a loc
# -> interrupt -> release -> close

vidloc = "/home/varshalalapura/Desktop/Inspiration/drop.avi"
cap = cv2.VideoCapture(vidloc)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(vidloc,fourcc,40,(640,480))

while True:
    ret, frame = cap.read()
    colour_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',frame)
    cv2.imshow('colour_frame', colour_frame)
    out.write(colour_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'): # dont write as "and"
        break

cap.release()
out.release()
cv2.destroyAllWindows()


