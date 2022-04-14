import cv2

imagePath = "../source image/frame.png"
img = cv2.imread(imagePath)
cv2.imshow('image',img)
cv2.waitKey(0)
img = cv2.circle(img, (110,126), 5, (255,0,0), -1)
img = cv2.circle(img, (449,147), 5, (255,0,0), -1)
img = cv2.circle(img, (79,527), 5, (255,0,0), -1)
img = cv2.circle(img, (420,550), 5, (255,0,0), -1)
cv2.imshow('image',img)
cv2.waitKey(0)
