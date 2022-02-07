# base template code
# press q to exit the code

import os
import cv2 as cv
import numpy as np

path_to_image = os.path.join(os.path.dirname(__file__), "images", "hand.jpeg")

img = cv.imread(path_to_image)

# stacking the images 
horizontal_stack = np.hstack([img, img])
vertical_stack = np.vstack([img, img])

# stacks the image horizontally
hor_win = "Horizontal Stacked Image"
cv.namedWindow(hor_win)
cv.moveWindow(hor_win, horizontal_stack.shape[1]*1, 0)
cv.imshow(hor_win, horizontal_stack)

# stacks the image vertically
vert_win = "Vertical Stacked Image"
cv.namedWindow(vert_win)
cv.moveWindow(vert_win, img.shape[1]*1, img.shape[0]*1)
cv.imshow(vert_win, vertical_stack)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()
        