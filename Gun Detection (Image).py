import numpy as np
import cv2
import imutils


gun_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread("Image_path")

frame = imutils.resize(img, width=500)

imgGr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

guns = gun_cascade.detectMultiScale(imgGr, 1.3, 5, minSize=(100,100))

gun_exist = len(guns) > 0 

for (x,y,w,h) in guns:
    frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
    
    cv2.putText(frame,'Firearm detected!',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,
                0.75,(0,255,255),2,cv2.LINE_AA)

cv2.imshow("Title_name", frame)
key=cv2.waitKey(0) & 0xFF

if key == ord('q'):
    cv2.destroyAllWindows()

if gun_exist:
    print("guns detected")
else:
    print("guns not detected")


cv2.destroyAllWindows()
