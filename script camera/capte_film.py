# USAGE
# python detect.py --images images

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import subprocess
import time

# initialize the HOG descriptor/person detector


# loop over the image paths
for i in range(1,300):
	
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	subprocess.call('sudo /home/test/raspberrypi/ArduCAM4Pi/ov2640_capture -c film/test'+str(i)+'.jpg 352x288',shell=True)
	time.sleep(0.1)
