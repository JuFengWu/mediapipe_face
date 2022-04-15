import cv2
import numpy as np

lennaPath = "../source image/Lenna.jpg"
imagePath = "../source image/book.png"

lennaImg = cv2.imread(lennaPath)
#cv2.imshow('origin lena',lennaImg)
#cv2.waitKey(0)

bookImg = cv2.imread(imagePath)
#cv2.imshow('origin book',bookImg)
#cv2.waitKey(0)

lennaPoints = np.array([[0,0],[316,0],[316,316],[0,316]])
boolPoints = np.array([[138,152],[296,40],[300,491],[136,652]])

h, status = cv2.findHomography(lennaPoints,boolPoints)

print(h)

maskPoint = np.array([[99,40],[139,28],[180,49],[213,87],[245,70],[252,101],[172,145],[89,238],[91,218],[73,108],[82,67]]).astype('float32')

print(maskPoint)

#newMaskPoint= cv2.warpPerspective(maskPoint, h, (11, 2))


newMaskPoint = cv2.perspectiveTransform(maskPoint[None, :, :],h)

print(newMaskPoint)

newMaskPoint = newMaskPoint.astype('int32')

print(newMaskPoint)

hatMask = np.zeros((bookImg.shape[0], bookImg.shape[1]), dtype=np.uint8)
cv2.fillPoly(hatMask, [newMaskPoint], (1,1,1))
cv2.imshow('hatMask', hatMask)
cv2.waitKey(0)

newImg = cv2.warpPerspective(lennaImg, h, (bookImg.shape[1], bookImg.shape[0]))

hatImg = cv2.bitwise_and(newImg, newImg, mask = hatMask)
cv2.imshow('hatImg', hatImg)
cv2.waitKey(0)

cv2.fillPoly(bookImg, [newMaskPoint], (0,0,0))
cv2.imshow('bookImg', bookImg)
cv2.waitKey(0)

newBookImg = cv2.add(bookImg, hatImg)
cv2.imshow('new book', newBookImg)
cv2.waitKey(0)
