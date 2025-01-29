import cv2
import numpy as np
#path=r"C:\Users\Sid\Downloads\git_commit.mp4"

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    ret,img=cap.read()
    #img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_white= np.array([0,0,200]) 
    upper_white = np.array([180,55,125])
    mask = cv2.inRange(hsv,lower_white,upper_white)
    mask_inv = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(img,img,mask=mask_inv)
    cv2.imshow('Video',result)
    cv2.waitKey(1)

