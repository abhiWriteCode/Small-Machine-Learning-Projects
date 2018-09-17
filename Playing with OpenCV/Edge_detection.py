import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
	edge = cv2.Canny(frame, 100, 100) # 2nd and 3rd args are our minVal and maxVal respectively

	cv2.imshow('Original', frame)
	# cv2.imshow('Laplacian', laplacian)
	# cv2.imshow('sobel x', sobelx)
	# cv2.imshow('sobel y', sobely)
	cv2.imshow('edge1', edge)

	if cv2.waitKey(5) & 0xFF == 32: # if press SPACE bar
		break

cap.release()
cv2.destroyAllWindows()