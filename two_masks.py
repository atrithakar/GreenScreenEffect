# This code is same as the other code but it uses two masks technique which was required for the colour of the blanket used in the video.
# The two mask technique is used when you want to deal with the lower and higher extreme values without involving mid values as in the case with my blanket.

import cv2 as cv
import numpy as np
import time
time.sleep(3)
back = cv.VideoCapture(0)
ret, background = back.read()
back.release()
lower = np.array([0, 175, 0])
upper = np.array([10, 255, 255])
lower1 = np.array([170, 175, 0])
upper1 = np.array([180, 255, 255])
video = cv.VideoCapture(0)
output = cv.VideoWriter('generated.mp4',cv.VideoWriter_fourcc(*'mp4v'),30,(640,480))
while True:
    success, img = video.read()
    image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask0 = cv.inRange(image, lower, upper)
    mask1 = cv.inRange(image, lower1, upper1)
    mask = cv.bitwise_or(mask0,mask1)
    img[mask!=0]=(0,0,0)
    result = cv.bitwise_or(img,background,mask=mask)
    final_result = cv.add(result,img)
    output.write(final_result)
    cv.imshow("final_result", final_result)
    cv.imshow("mask", mask)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv.destroyAllWindows()