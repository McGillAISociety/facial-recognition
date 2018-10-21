import numpy as np
import cv2


def start_inference(ip,weight_address,frame_preview):

	if (ip == None):
		cap = cv2.VideoCapture(0)
	else:
		cap = cv2.VideoCapture(ip)

	face_cascade = cv2.CascadeClassifier(weight_address)
	cv2.namedWindow("output", cv2.WINDOW_NORMAL)
	cv2.resizeWindow('output', 600,600)

	while(True):
		# Capture frames
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		detected = False
		# Loop through faces and draw bounding box 
		for (x,y,w,h) in faces:
			cv2.putText(frame,"Face",(x,y-5),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2,cv2.LINE_AA)
			
			if (frame_preview):
				draw_preview(frame,(x,y,w,h))

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
		cv2.imshow('output',frame)


		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

# Preprocesses frame
def preprocess_frame(frame):
	pass

# Overwrites frame with preview image of bounding box in top left corner
def draw_preview(frame,box_coords):
	# Draw preview in left corner
	x,y,w,h = box_coords
	preview = cv2.resize(frame[y:y+h,x:x+w], (0,0), fx=0.5, fy=0.5)
	ph,pw = preview.shape[:2]
	frame[0:ph,frame.shape[1]-pw:frame.shape[1]] = preview

