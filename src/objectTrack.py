# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import os



frames=[]
saveFrames=True

def writeFrames( filename ):
	# write video from numpy arrays via cv2
	out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*"mp4v"), 30, (512,512))
	for frame in frames:
		out.write(frame)
	
	out.release()
	# reencode video with ffmpeg
	os.system("ffmpeg -y -i " + filename + " -vcodec libx264 " + filename + "&>/dev/null")

def trackVideo( filename ):
	raw = np.zeros(shape=(100,3))
	count = 0

	# define the lower and upper boundaries of the "green"
	# ball in the HSV color space, then initialize the
	# list of tracked points
	greenLower = (29, 86, 6)
	greenUpper = (64, 255, 255)

	pts = deque(maxlen=100)
	vs = cv2.VideoCapture(filename)


	# keep looping
	while True:
		# grab the current frame
		(grabbed, frame) = vs.read()
		# handle the frame from VideoCapture or VideoStream
		# if we are viewing a video and we did not grab a frame,
		# then we have reached the end of the video
		if not grabbed:
			break
		# resize the frame, blur it, and convert it to the HSV
		# color space
		#frame = imutils.resize(frame)
		
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	
		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, greenLower, greenUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		# find contours in the mask and initialize the current
		# (x, y) center of the ball
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		center = None
		# only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			# only proceed if the radius meets a minimum size
			if radius > 1:
				#Add the tracked values to raw for later processing
				raw[count] = [x,y,radius]
				count+=1
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv2.circle(frame, (int(x), int(y)), int(radius),
					(0, 0, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
		# update the points queue
		pts.appendleft(center)
	
		

	# loop over the set of tracked points
		for i in range(1, len(pts)):
			# if either of the tracked points are None, ignore
			# them
			if pts[i - 1] is None or pts[i] is None:
				continue
			# otherwise, compute the thickness of the line and
			# draw the connecting lines
			thickness = int(np.sqrt(100 / float(i + 1)) * 2.5)
			cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

		#Save current frame to global array if enabled
		if saveFrames:
			frames.append(frame)
		
		key = cv2.waitKey(1) & 0xFF
		# if the 'q' key is pressed, stop the loop
		if key == ord("q"):
			break
	
	vs.release()
	print(len(frames))

	return raw
