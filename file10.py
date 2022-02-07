#!/usr/bin/env python3
# base template code
# press q to exit the code

import os
import cv2 as cv
import numpy as np
from utils import stackImages

path_to_image = os.path.join(os.path.dirname(__file__), "images", "hand.jpeg")


def empty(value):
    pass


window_name = "TrackBars"
cv.namedWindow(window_name)
cv.resizeWindow("TrackBars", 640, 240)
cv.createTrackbar("Hue Minimum", window_name, 0, 179, empty)
cv.createTrackbar("Hue Maximum", window_name, 179, 179, empty)
cv.createTrackbar("Saturation Minimum", window_name, 0, 255, empty)
cv.createTrackbar("Saturation Maximum", window_name, 255, 255, empty)
cv.createTrackbar("Value Minimum", window_name, 0, 255, empty)
cv.createTrackbar("Value Maximum", window_name, 255, 255, empty)

while True:
    
    img = cv.imread(path_to_image)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    hue_minimum = cv.getTrackbarPos("Hue Minimum", window_name)
    hue_maximum = cv.getTrackbarPos("Hue Maximum", window_name)
    
    saturation_minimum = cv.getTrackbarPos("Saturation Minimum", window_name)
    saturation_maximum = cv.getTrackbarPos("Saturation Maximum", window_name)
    
    value_minimum = cv.getTrackbarPos("Value Minimum", window_name)
    value_maximum = cv.getTrackbarPos("Value Maximum", window_name)
    
    print(hue_minimum, hue_maximum, saturation_minimum, saturation_maximum, value_minimum, value_maximum)
    
    lower = np.array([hue_minimum, saturation_minimum, value_minimum])
    upper = np.array([hue_maximum, saturation_maximum, value_maximum])
    mask = cv.inRange(imgHSV, lower, upper)
    
    imgResult = cv.bitwise_and(img, img, mask=mask)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv.imshow("Stacked Images", imgStack)

    cv.waitKey(1)
