#!/usr/bin/env python
import cv2
import os
import shutil
import sys

source = sys.argv[1]
movie = cv2.VideoCapture(source)

folder = 'Frames'
shutil.rmtree(folder)
os.mkdir(folder)

count = 0
while True:
    success,image = movie.read()
    if not success:
        break
    if count%20 == 0:
        cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extacted in {}.".format(count,folder))