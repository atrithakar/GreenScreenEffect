'''
Project name: Green Screen Effect Using OpenCV
Author name: Thakar Atri Kamleshkumar
Mentor name: Amit Gohel
Date of Completion: 1st April, 2023
'''

import cv2 as cv
import numpy as np

# Use the following 5 lines of code for harry potter effect and if you don't want to do so you can comment them and uncomment that other piece of code.
import time
time.sleep(3)
back = cv.VideoCapture(0)
ret, background = back.read()
back.release()

# Uncomment below line to set a background of some other image.
# background = cv.imread('background.jpg')

# Tweak the values of below two variables to apply greenscreen effect to the colour of your choice.
# Note that these values are hsv values and use hsv chart provided to tweak the values.
lower = np.array([0, 175, 0])
upper = np.array([10, 255, 255])

video = cv.VideoCapture(0)

# Tweak the value of last argument of below line of code according to the resolution of your camera.
output = cv.VideoWriter('generated.mp4',cv.VideoWriter_fourcc(*'mp4v'),30,(640,480))

while True:
    success, img = video.read()
    image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(image, lower, upper)
    img[mask!=0]=(0,0,0)
    result = cv.bitwise_or(img,background,mask=mask)
    final_result = cv.add(result,img)
    output.write(final_result)
    cv.imshow("final_result", final_result)
    # Press q to turn off the video. You can also tweak values according to your desires.
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()