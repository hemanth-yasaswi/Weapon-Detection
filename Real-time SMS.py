import numpy as np
import cv2
import imutils
import datetime
from twilio.rest import Client

account_sid = 'AC2d9477048f524448a962c5230df5c1da'
auth_token = 'b5fac05688170d7301477bbc93ccb6f7'
twilio_phone_number = '+14154134320'
recipient_phone_numbers = '+919618462110', 

gun_cascade = cv2.CascadeClassifier('cascade.xml')

camera = cv2.VideoCapture('Videos/Stock4.mp4')
firstFrame = None

client = Client(account_sid, auth_token)

notification_sent = False

while True:
    ret, frame = camera.read()
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    if len(guns) > 0 and not notification_sent:
        for phone_number in recipient_phone_numbers:
            message = client.messages.create(
                body='Firearm detected!',
                from_=twilio_phone_number,
                to=phone_number
            )
            print(f"SMS notification sent to {phone_number}!")
        notification_sent = True

    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.putText(frame, 'Firearm detected!', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)

    cv2.imshow("Security Feed", frame)

    if len(guns) == 0:
        notification_sent = False

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()