#!/usr/bin/env python
from get_weights import Weights
import cv2
import os
import time
import shutil
import re
import sys

def tryint(s):
	try:
		return int(s)
	except:
		return s

def alphanum_key(s):
	return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
	l.sort(key=alphanum_key)

frame_folder='/data/gpuuser2/neuraldiary/Frames' # location of your folder where the frames are.
files = os.listdir(frame_folder)
print 'Found ' + str(len(files)) + ' in the folder ' + frame_folder + '. Sorting...'
sort_nicely(files)

time.sleep(1)
NN = Weights()

target_folder = '/data/gpuuser2/neuraldiary/Sampled' # location of the destination folder where you want your output.
try:
	shutil.rmtree(target_folder)
except OSError:
	pass

try:
	os.mkdir(target_folder)
except:
	pass

i = 0

img_init = os.path.join(frame_folder, files[0])
#th = sys.argv[1]
for j in range(0,len(files)):
	img_next = os.path.join(frame_folder,files[j])
	n = NN.comp_image(img_init, img_next)		# generates the norm difference of two images

	if n*1.0 > 10.0: # vary the parameter as per requirement
		img_init = img_next
		median = (i+j)/2 	# the frame in the middle is selected to represent the range
		i = j
		print 'copying file: ' + files[median] + ', ' + str(median) + ', n=' + str(n) + ', i=' + str(i)
		shutil.copy2(os.path.join(frame_folder, files[median]), target_folder)
