import cv2

imagePath = "../source image/Lenna.jpg"
img = cv2.imread(imagePath)
cv2.imshow('image',img)
cv2.waitKey(0)
img = cv2.circle(img, (99,40), 5, (255,0,0), -1)
img = cv2.circle(img, (139,28), 5, (255,0,0), -1)
img = cv2.circle(img, (180,49), 5, (255,0,0), -1) 
img = cv2.circle(img, (213,87), 5, (255,0,0), -1)
img = cv2.circle(img, (255,70), 5, (255,0,0), -1)
img = cv2.circle(img, (252,101), 5, (255,0,0), -1)
img = cv2.circle(img, (172,145), 5, (255,0,0), -1)
img = cv2.circle(img, (89,238), 5, (255,0,0), -1)
img = cv2.circle(img, (91,218), 5, (255,0,0), -1)
img = cv2.circle(img, (93,181), 5, (255,0,0), -1)
img = cv2.circle(img, (73,108), 5, (255,0,0), -1)
img = cv2.circle(img, (82,67), 5, (255,0,0), -1)
cv2.imshow('image',img)
cv2.waitKey(0)

