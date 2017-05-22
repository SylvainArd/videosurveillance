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

img=cv2.imread("film/test1.jpg")
if img is None or img.shape[0]==0 :
	print("image erronnee")
