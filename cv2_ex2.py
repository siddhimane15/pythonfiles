import cv2

path=r"C:\Users\Sid\Pictures\Saved Pictures\world-environment.png"

img=cv2.imread(path)
img2=cv2.resize(img,(1280,720))
img3 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image',img3)
cv2.waitKey