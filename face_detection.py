#A simple face detection program that uses haar cascades to detect faces
import cv2 as cv
haar_cascade=cv.CascadeClassifier('haar_face.xml') #setting up our classifier

capture=cv.VideoCapture(0) #creating a capture variable to capture video from the webcam
#setting up an infinite loop to analyze video frame by frame
while True:
    isTrue, frame=capture.read()
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces=haar_cascade.detectMultiScale(gray, 1.1, 4) #detecting the faces in the frame
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2) #drawing a rectangle on the frame
    cv.imshow('Frame', frame)
    k=cv.waitKey(30) and 0xff
    if k==27: 
        break #breaks when escape key is pressed
capture.release()