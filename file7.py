#!/usr/bin/env python3
# press q to exit the code
# warp perspective here

# Perspective Transformation :
# In Perspective Transformation, we can change the perspective of a given image or video for 
# getting better insights into the required information. In Perspective Transformation, we need to 
# provide the points on the image from which want to gather information by changing the perspective.
# We also need to provide the points inside which we want to display our image. 
# Then, we get the perspective transform from the two given sets of points and wrap it with the 
# original image.


import os
import cv2 as cv
import numpy as np

path_to_image = os.path.join(os.path.dirname(__file__), "images", "warp.jpeg")

img = cv.imread(path_to_image)
height, width, _ = img.shape

# these are the image coordinates taken from topleft, bottomleft, bottomright, topright
topleft = [3, 60]
bottomleft = [57, 157]
bottomright = [63, 23]
topright = [122, 124]

img_coordinates = np.float32([topleft, bottomleft, bottomright, topright])

topleft_perspective = [0,0]
bottomleft_perspective = [width,0]
bottomright_perspective = [0,height]
topright_perspective = [width,height]

# you need to tell which corner of the image is which one, this matrix tells that
perspective_teller = np.float32([topleft_perspective, bottomleft_perspective, bottomright_perspective, topright_perspective])

matrix = cv.getPerspectiveTransform(img_coordinates, perspective_teller)
img_output = cv.warpPerspective(img, matrix, (width,height))

win = "Warp Image"
cv.namedWindow(win)
cv.moveWindow(win, img_output.shape[1]*1, 0)
cv.imshow(win, img_output)



if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()    