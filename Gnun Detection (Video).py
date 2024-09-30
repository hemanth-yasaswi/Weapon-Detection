import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')

video_path = 'Videos/Stock2.mp4'
camera = cv2.VideoCapture(video_path)

while True:
    ret, frame = camera.read()
    if not ret:
        break  

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    for (x, y, w, h) in guns:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.putText(frame,'Firearm detected!',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,
                    0.75,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(frame,
                datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10,frame.shape[0]-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35,(0,255,255),
                1)

    cv2.imshow("Security Feed", frame)

    key = cv2.waitKey(30) & 0xFF 
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()