import cv2 as cv

for _ in [i for i in dir(cv) if i.startswith('FONT_')]:
    print(_)