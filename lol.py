import cv2
import numpy as np
'''
img = cv2.imread("1.jpg")
lower_blue = np.array([111,94,6])
upper_blue = np.array([240,181,74])
lower_yellow = np.array([0,121,156])
upper_yellow = np.array([127,251,253])
list_color = [(lower_yellow, upper_yellow), (lower_blue, upper_blue)]

for j in range(len(list_color)):
	mask = cv2.inRange(img, list_color[j][0], list_color[j][1])

	center = None

	point = []

	# finds contours 
	contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)[-2]
	# loop throught the contours array
	for i in range(len(contours)):
		# gets parameters for circles
		c = contours[i]
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		# if statement to prevent contours that are too small to break the program
		if M["m00"] == 0:
			continue
		else:	
			# computes centre
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	
			# only proceed if the radius meets a minimum size
			if radius > 100 and j == 0:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
				#cv2.circle(img, (int(x), int(y)), int(radius),
				#	(0, 255, 255), 2)
				# stores all the points in a array
				point.append(center)
				#cv2.circle(img, center, 5, (0, 0, 255), -1)
				print("yellow")
			elif radius > 100 and j == 1:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
				#cv2.circle(img, (int(x), int(y)), int(radius),
				#	(0, 255, 255), 2)
				# stores all the points in a array
				point.append(center)
				#cv2.circle(img, center, 5, (0, 0, 255), -1)
				print("greeen")


x1 = (point[0][0] + point[2][0])/2
y1 = (point[0][1] + point[2][1])/2
x2 = (point[1][0] + point[3][0])/2
y2 = (point[1][1] + point[3][1])/2

x_avg = (x1 + x2)/2
y_avg = (y1 + y2)/2

cv2.circle(img, (x_avg,y_avg), 5, (0, 0, 255), -1)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

cap = cv2.VideoCapture(0)

lower_blue = np.array([111,94,6])
upper_blue = np.array([240,181,74])
lower_red = np.array([2,6,121])
upper_red = np.array([63,75,255])
list_color = [(lower_red, upper_red), (lower_blue, upper_blue)]

while(1):
	# Take each frame
	_, frame = cap.read()

	for j in range(len(list_color)):
		mask = cv2.inRange(frame, list_color[j][0], list_color[j][1])
		res = cv2.bitwise_and(frame,frame, mask= mask)
		median = cv2.medianBlur(res,15)
	
		center = None
	
		point = []
	
		# finds contours 
		contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)[-2]
		# loop throught the contours array
		for i in range(len(contours)):
			# gets parameters for circles
			c = contours[i]
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			# if statement to prevent contours that are too small to break the program
			if M["m00"] == 0:
				continue
			else:	
				# computes centre
				center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		
				# only proceed if the radius meets a minimum size
				if radius > 20 and j == 0:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
					#cv2.circle(img, (int(x), int(y)), int(radius),
					#	(0, 255, 255), 2)
					# stores all the points in a array
					point.append(center)
					#cv2.circle(img, center, 5, (0, 0, 255), -1)
					print("red")
				elif radius > 20 and j == 1:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
					#cv2.circle(img, (int(x), int(y)), int(radius),
					#	(0, 255, 255), 2)
					# stores all the points in a array
					point.append(center)
					#cv2.circle(img, center, 5, (0, 0, 255), -1)
					print("blue")


				cv2.imshow('mask',mask)
				cv2.imshow('Median Blur',median)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
	        break

cv2.destroyAllWindows()

#(8, 118, 16, 89, 255, 142)

