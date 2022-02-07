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

resize_ht = 200
resize_wt = 300

# tuple provided is (width, height)
resized_img = cv.resize(img, (resize_wt, resize_ht))

res_win = "Resized Image"
cv.namedWindow(res_win)
cv.moveWindow(res_win, img.shape[1]*2, 0)
cv.imshow(res_win, resized_img)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()
        