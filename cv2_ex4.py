import cv2
import numpy as np

path=r"C:\Users\Sid\Pictures\Saved Pictures\air pollution.jpeg"


img=cv2.imread(path)
img2=cv2.resize(img,(640,480))
hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
lower_white= np.array([0,0,200]) 
upper_white = np.array([180,55,255])
mask = cv2.inRange(hsv,lower_white,upper_white)
mask_inv = cv2.bitwise_not(mask)
result = cv2.bitwise_and(img2,img2,mask=mask_inv)
#img3=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image',result)
cv2.waitKey(0)