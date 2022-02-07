# base template code
# press q to exit the code

import os
import cv2 as cv
import numpy as np

path_to_image = os.path.join(os.path.dirname(__file__), "images", "hand.jpeg")

img = cv.imread(path_to_image)

win = "Original Image"
cv.namedWindow(win)
cv.moveWindow(win, img.shape[1]*1, 0)
cv.imshow(win, img)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()
        