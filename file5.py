# base template code
# press q to exit the code

import os
import cv2 as cv
import numpy as np

black_win_size = (512, # height
                  512, # width
                  3)   # channels (values 1, 3 and 4 permitted only)

black_img = black_img_patch = np.zeros(black_win_size, np.uint8)

black_win = "Black Window"
cv.namedWindow(black_win)
cv.moveWindow(black_win, black_win_size[1]*1, 0)
cv.imshow(black_win, black_img)

start_ht = 0
end_ht = black_win_size[0]//2

start_wt = 0
end_wt = black_win_size[1]//2

black_img_patch[start_ht:end_ht, start_wt:end_wt] = 255,0,0

black_patch_win = "Black Patch Window"
cv.namedWindow(black_patch_win)
cv.moveWindow(black_patch_win, black_win_size[1]*2, 0)
cv.imshow(black_patch_win, black_img_patch)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()
        