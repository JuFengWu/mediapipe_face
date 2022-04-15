import cv2

imagePath = "../source image/book.png"
img = cv2.imread(imagePath)
cv2.imshow('image',img)
cv2.waitKey(0)
img = cv2.circle(img, (138,152), 5, (255,0,0), -1)
img = cv2.circle(img, (296,40), 5, (255,0,0), -1)
img = cv2.circle(img, (300,491), 5, (255,0,0), -1) 
img = cv2.circle(img, (136,652), 5, (255,0,0), -1) # book png four points
cv2.imshow('image',img)
cv2.waitKey(0)

