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
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# loop over the image paths
for i in range(1,10):
	
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	subprocess.call('sudo /home/test/raspberrypi/ArduCAM4Pi/ov2640_capture -c test/test'+str(i)+'.jpg 320x240',shell=True)
	debut=time.time()
	image = cv2.imread('test/test'+str(i)+'.jpg')
	#image = imutils.resize(image, width=min(400, image.shape[1]))
	orig = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)

	# draw the original bounding boxes
	#for (x, y, w, h) in rects:
		#cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        print(time.time()-debut);
	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)



	# show the output images
	#cv2.imshow("Before NMS", orig)
	#cv2.imshow("After NMS", image)
	print(time.time()-debut);
	cv2.imwrite('test/test'+str(i)+'_traite.jpg',image)
	time.sleep(0.2)