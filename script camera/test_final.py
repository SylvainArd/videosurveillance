from __future__ import print_function

from imutils.object_detection import non_max_suppression

from imutils import paths

import imutils

import numpy as np

import time

import cv2

import math
import subprocess


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

	

def carre(x):

	return x*x;

	

def afficheImage(img):

	img = imutils.resize(img, width=min(400, img.shape[1]))

	cv2.imshow("Video", img)

	cv2.waitKey(1)

			



cap = cv2.VideoCapture('test.mov')







# params for ShiTomasi corner detection



feature_params = dict( maxCorners = 500,



                       qualityLevel = 0.01,



                       minDistance = 10,



                       blockSize = 3 )







# Parameters for lucas kanade optical flow



lk_params = dict( winSize  = (31,31),



                  maxLevel = 3,



                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 0.03))







# Create some random colors



color = np.random.randint(0,255,(100,3))

#for i in range(1,100):

		#ret, frame = cap.read()



def capte_image(i):
	#return cv2.imread('film/test'+str(i)+'.jpg')
	subprocess.call('sudo /home/test/raspberrypi/ArduCAM4Pi/ov2640_capture -c test/image.jpg 320x240',shell=True)
	time.sleep(0.2)
	frame = cv2.imread('test/image.jpg')
	return imutils.resize(frame, width=min(400, frame.shape[1]))#retaille la frame a 400

#ret, frame = cap.read()#on capte la premiere frame

frame = capte_image(1)
frame = imutils.resize(frame, width=min(400, frame.shape[1]))#retaille la frame a 400

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#on calcule son image en niveaux de gris



a_silhouette=0#indique si on a trouve une silhouette

dr_image_avec_silhouette=gray.copy()#derniere image contenant une silhouette que l'on initialise arbitrairement a gray

ii=1

while(1):

	ii=ii+1

	k = cv2.waitKey(30) & 0xff



	if k == 27:



		break

	print("frame "+str(ii))
	
	#on stocke l'ancienne frame en niveaux de gris dans old_frame et l'ancienne frame dans old_frame

	old_frame=frame.copy()

	old_gray=gray.copy()

	temps=time.time()
	frame = capte_image(ii)
	temps=time.time()-temps
	print("temps de captage d'image :"+str(temps))

	frame = imutils.resize(frame, width=min(400, frame.shape[1]))

	img=frame



	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



	if not a_silhouette:#si pas de silhouette on en recherche une

		temps=time.time()

		pick, image_=silhouette(frame)#on recherche une silhouette
		temps=time.time()-temps
		print("temps detection silhouette :"+str(temps))

		if (len(pick)==0):#si on en trouve toujours pas

			afficheImage(img)

			continue;#on passe a la frame suivante



		else:#sinon



			#on dessine le rectangle de la silhouette



			for (xA, yA, xB, yB) in pick:



				cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)



			a_silhouette=1

			dr_image_avec_silhouette=gray.copy()



			#s'il ya une silhouette on cherche des points d'interet sur la silhouette



			#on cree un masque de 0 pour tout refuser



			mask_=np.zeros_like(gray)#zeros_like prend la meme largeur, hauteur et type que frame et met des 0 dedans



			#on dessine des rectangles blancs sur les silhouettes pour autoriser la recherche de silhouette dessus



			for (xA, yA, xB, yB) in pick:



				cv2.rectangle(mask_, (xA, yA), (xB, yB), 255, 2)



			#on calcule les points d'interet que sur la silhouette grace au masque



			p0 = cv2.goodFeaturesToTrack(gray, mask = mask_, **feature_params)

			afficheImage(img)
			
			print("silhouette trouvee !")

			continue#force a calculer la frame suivante



			

	if a_silhouette:

		temps=time.time()





		

		# calculate optical flow

		#calcule le flot optique

		p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, gray, p0, None, **lk_params)

		#on enleve les points d'interets qui n'ont pas beaucoup bouges

		for i in range(len(p0)):

			if st[i]:

				if math.sqrt(carre(p1[i][0][0]-p0[i][0][0])+carre(p1[i][0][1]-p0[i][0][1]))<0.5:

					st[i]=0

		#cree un masque pour cacher les nouveaux points d'interets 

		mask_=np.zeros_like(gray)

		mask_[:]=255

		for i in range(len(p1)):#nouveaux points d'interets

			cv2.circle(mask_,(np.int32(p1[i][0][0]),np.int32(p1[i][0][1])),5,0,-1)

			

		p0 = cv2.goodFeaturesToTrack(gray, mask = mask_, **feature_params)#recalcule es points d'interets

		

		#on calcule la somme des status (qui valent 0 dans le cas des points d'interets disparus et 1 dans le cas des points d'interet suivis)

		somme=np.ndarray.sum(st)

		if (somme==0):#si tous les points d'interet ont disparus

			a_silhouette=0

			afficheImage(img)

			print("tous les points d'interet nt disparus !")

			continue#on force la calcul d'une autre frame pour rechercher une silhouette

		



		# Select good points



		good_new = p1[st==1]



		good_old = p0[st==1]



		# Create a mask image for drawing purposes



		mask = np.zeros_like(old_frame)



		# draw the tracks



		for i,(new,old) in enumerate(zip(good_new,good_old)):



			a,b = new.ravel()



			c,d = old.ravel()



			cv2.circle(img,(a,b),5,color[i].tolist(),-1)#on affiche les points d'interets suivis



		afficheImage(img)

		p0 = good_new.reshape(-1,1,2)

		temps=time.time()-temps
		print("temps de la detection des points d'interets : "+str(temps))









	# Now update the previous frame and previous points





	



	







cv2.destroyAllWindows()



cap.release()



