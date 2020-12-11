import cv2
import numpy as np
import requests

class VideoCamera(object):
    def __init__(self):

        self.video = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        self.out = cv2.VideoWriter('record.avi', fourcc, 20.0, (640, 480))

    
    def __del__(self):
        self.video.release()
        self.out.release()
    
    def get_frame(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        success, image = self.video.read()

        gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.flip(image,180)
        faces = face_cascade.detectMultiScale(image, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),3)
            roi_color = image[y:y+h, x:x+w]
            roi_gray= gray[y:y+h, x:x+w]
            eyes= eye_cascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255, 0, 255), 2)
        ret, jpeg = cv2.imencode('.jpg', image)


        return jpeg.tobytes()      

               

        

        

