#!/usr/bin/env python3
# press q to exit the code

import os
import cv2 as cv
import numpy as np

path_to_image = os.path.join(os.path.dirname(__file__), "images", "hand.jpeg")

img = cv.imread(path_to_image)

height, width, channels = img.shape

print(img.shape)

win = "Original Image"
cv.namedWindow(win)
cv.moveWindow(win, img.shape[1]*1, 0)
cv.imshow(win, img)

start_ht = 0
end_ht = height//2

start_wt = 0
end_wt = width//2

# here the height, width is to be mentioned in the cropped image vis-a-vis in resize function
crop_img = img[start_ht:end_ht,start_wt:end_wt]

crop_win = "Cropped Image"
cv.namedWindow(crop_win)
cv.moveWindow(crop_win, img.shape[1]*2, 0)
cv.imshow(crop_win, crop_img)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()
        