
import cv2
import numpy as np

path = r'C:\Users\Sid\Pictures\Saved Pictures\world-environment.png'

img = cv2.imread(path)
img = cv2.resize(img,(640,480)) 

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_green = np.array([0,1,0])
upper_green = np.array([127,255,127])

mask = cv2.inRange(hsv,lower_green,upper_green)
masked_img = cv2.bitwise_and(img,img,mask=mask)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image',masked_img)
cv2.waitKey(0)
