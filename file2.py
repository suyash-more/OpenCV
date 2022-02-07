#!/usr/bin/env python3
# press q to exit the code

import os
import cv2 as cv
import numpy as np

path_to_image = os.path.join(os.path.dirname(__file__), "images", "hand.jpeg")
kernel = np.ones((5,5), np.uint8)

img = cv.imread(path_to_image)

height, width, channels = img.shape

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(7,7),0)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
canny = cv.Canny(img, 150, 200)
dilation = cv.dilate(canny, kernel, iterations=1)
eroded = cv.erode(dilation, kernel, iterations=1)

win1 = "Original Image"
cv.namedWindow(win1)
cv.moveWindow(win1,width*1, 0)
cv.imshow(win1, img)

win2 = "Gray Image"
cv.namedWindow(win2)
cv.moveWindow(win2,width*2, 0)
cv.imshow(win2, gray)

win3 = "Blurr Image"
cv.namedWindow(win3)
cv.moveWindow(win3,width*3, 0)
cv.imshow(win3, blur)

win4 = "HSV Image"
cv.namedWindow(win4)
cv.moveWindow(win4,width*4, 0)
cv.imshow(win4, hsv)

# sometimes you want to detect lines in the image (so use canny)
win5 = "Canny Image"
cv.namedWindow(win5)
cv.moveWindow(win5,width*5, 0)
cv.imshow(win5, canny)

# morphology image methods

# Dilation:
# Dilation expands the image pixels i.e. it is used for expanding an element A by using structuring element B.
# Dilation adds pixels to object boundaries.
# The value of the output pixel is the maximum value of all the pixels in the neighborhood. 
# A pixel is set to 1 if any of the neighboring pixels have the value 1.
win6 = "Dilated Image"
cv.namedWindow(win6)
cv.moveWindow(win6,width*6, 0)
cv.imshow(win6, dilation)

# Erosion:
# Erosion shrink-ens the image pixels i.e. it is used for shrinking of element A by using element B.
# Erosion removes pixels on object boundaries.:
# The value of the output pixel is the minimum value of all the pixels in the neighborhood. 
# A pixel is set to 0 if any of the neighboring pixels have the value 0.
win7 = "Eroded Image"
cv.namedWindow(win7)
cv.moveWindow(win7,width*7, 0)
cv.imshow(win7, eroded)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()