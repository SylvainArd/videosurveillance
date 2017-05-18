from __future__ import print_function
import cv
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import sys

def silhouette(image):
	# initialize the HOG descriptor/person detector
	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
	image = imutils.resize(image, width=min(400, image.shape[1]))
	orig = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),padding=(8, 8), scale=1.05)
	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
	

	
	return pick, image
	

	
def diffImg(t0, t1, t2):
	d1 = cv2.absdiff(t2, t1)
	d2 = cv2.absdiff(t1, t0)
	return cv2.bitwise_and(d1, d2)

def img400g(image):
	image= imutils.resize(image, width=min(400, image.shape[1]))
	return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
		
cap = cv2.VideoCapture( 'test.mov' )#ouverture de la video

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Read three images first:
t_minus = img400g(cap.read()[1])
t = img400g(cap.read()[1])
t_plus=img400g(cap.read()[1])
pick_rectangle=[]
while True:
	cv2.imshow( "Gradient", diffImg(t_minus, t, t_plus) )
	t_minus = t
	t = t_plus
	t_plus = img400g(cap.read()[1])
	pick, image=silhouette(t_plus)
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
	# show the output images
	cv2.imshow("Video", image)
	if cv2.waitKey(1) & 0xFF == ord('q'):#si on appuie sur q
		break
  


