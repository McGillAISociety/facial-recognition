import numpy as np
import cv2

def start_inference(ip,weight_address):
	cap = cv2.VideoCapture(ip)
	face_cascade = cv2.CascadeClassifier(weight_address)

	while(True):
		# Capture frames
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		detected = False
		# Loop through faces and draw bounding box 
		for (x,y,w,h) in faces:
			cv2.putText(frame,"Face",(x,y-5),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2,cv2.LINE_AA)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			detected = True

		# Draw left hand text if face recognized
		if (detected):
			cv2.putText(frame,"FACE DETECTED",(5,20),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2,cv2.LINE_AA)
		else:
			cv2.putText(frame,"NO FACE",(5,20),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2,cv2.LINE_AA)

		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Display the resulting frame
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

