import cv2
import numpy as np

lennaPath = "../source image/Lenna.jpg"
imagePath = "../source image/book.png"

lennaImg = cv2.imread(lennaPath)
cv2.imshow('origin lena',lennaImg)
cv2.waitKey(0)

bookImg = cv2.imread(imagePath)
cv2.imshow('origin book',bookImg)
cv2.waitKey(0)

lennaPoints = np.array([[0,0],[316,0],[316,316],[0,316]])
boolPoints = np.array([[138,152],[296,40],[300,491],[136,652]])

h, status = cv2.findHomography(lennaPoints,boolPoints)

print(type(lennaImg))

newImg = cv2.warpPerspective(lennaImg, h, (bookImg.shape[1], bookImg.shape[0]))

cv2.imshow('new lena',newImg)
cv2.waitKey(0)

cv2.fillConvexPoly(bookImg, boolPoints.astype(int), 0, 16)
cv2.imshow('new book',bookImg)
cv2.waitKey(0)

newBookImg = cv2.add(bookImg, newImg)
cv2.imshow('final image',newBookImg)
cv2.waitKey(0)
