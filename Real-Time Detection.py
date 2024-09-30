import numpy as np
import cv2
import imutils
import datetime


gun_cascade = cv2.CascadeClassifier('cascade.xml')


camera = cv2.VideoCapture(0)
firstFrame = None

while True:
    
    ret, frame = camera.read()
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    for (x, y, w, h) in guns:
       
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        
        cv2.putText(frame,'Firearm detected!',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,
                    0.75,(0,255,255),2,cv2.LINE_AA)

    
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)

   
    cv2.imshow("Security Feed", frame)

   
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()