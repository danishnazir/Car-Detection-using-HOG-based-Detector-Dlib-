import dlib
import cv2
import cvutils 
import sys
import os
import time
from skimage import io
#load car detector
detector = dlib.fhog_object_detector("car_detector.svm")
win = dlib.image_window()
#load video and process frame by frame
cap = cv2.VideoCapture('DSC_0004.MOV')
while(True):
#     # Capture frame-by-frame
     ret, frame = cap.read()
     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

     dets = detector(frame)
    

     for d in dets:
         cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
        
#     # Display the resulting frame
     cv2.imshow("frame",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
