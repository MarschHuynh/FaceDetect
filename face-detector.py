import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('speedSign.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cam = cv2.VideoCapture(0)
cam.set(3, 320) # set width 
cam.set(4, 240) # set height


while (True):
    rval, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    cv2.imshow('img', img)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
