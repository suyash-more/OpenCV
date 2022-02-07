#!/usr/bin/env python3
import cv2 as cv

for _ in [i for i in dir(cv) if i.startswith('COLOR_')]:
    print(_)