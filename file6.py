#!/usr/bin/env python3
# base template code
# press q to exit the code

import cv2 as cv
import numpy as np

height, width, channels = (512, 512, 3)
black_win_size = (height,
                  width,
                  channels) # (values 1, 3 and 4 permitted only)

black_img = np.zeros(black_win_size, np.uint8)

########################################################################################
# convention = (width, height)
line_start_px = (0, 0)
line_end_px = (100, 150)

# convention = (blue, green, red)
line_color = (255, 0, 0)

line_thickness = 3

cv.line(black_img, line_start_px, line_end_px, line_color, line_thickness)

########################################################################################
# convention = (width, height)
rect_start_px = (0, 0)
rect_end_px = (450, 40)

# convention = (blue, green, red)
rect_color = (0, 255, 0)

# can put in the thickness instead of cv.FILLED to get a non filled rectangle
cv.rectangle(black_img, rect_start_px, rect_end_px, rect_color, cv.FILLED)

########################################################################################
# convention = (width, height)
circ_centre_px = (width // 2, height // 2)
circ_radius = 30

# convention = (blue, green, red)
circ_color = (0, 0, 255)

circ_thickness = 3

cv.circle(black_img, circ_centre_px, circ_radius,circ_color, circ_thickness)
########################################################################################
# convention = (width, height)
text_px = (100, 400)
text_font = cv.FONT_HERSHEY_SIMPLEX

# fractional scale is also allowed 0.5, 1, 2 etc 
text_scale =  2

# convention = (blue, green, red)
text_color = (255, 255, 0)
text_thickness = 1

cv.putText(black_img, "Hello World", text_px, text_font, text_scale, text_color, text_thickness)
########################################################################################

black_win = "Black Window"
cv.namedWindow(black_win)
cv.moveWindow(black_win, black_win_size[1]*1, 0)
cv.imshow(black_win, black_img)


if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()
