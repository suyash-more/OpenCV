#!/usr/bin/env python3
# press q to exit the code

import os
import cv2 as cv

path_to_image = os.path.join(os.path.dirname(__file__), "images", "faces.jpg")
cascade_file = os.path.join(os.path.dirname(__file__), "cascade", "haarcascade_frontalface_default.xml")

faceCascade= cv.CascadeClassifier(cascade_file)

img = cv.imread(path_to_image)
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv.imshow("Result", img)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    exit()