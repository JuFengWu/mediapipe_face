import cv2
import numpy as np

imagePath = "../source image/Lenna.jpg"
img = cv2.imread(imagePath)
h,w,c = img.shape

mask = np.zeros((h, w), dtype=np.uint8)

pts = np.array([[99,40],[139,28],[180,49],[213,87],[245,70],[252,101],[172,145],[89,238],[91,218],[73,108],[82,67]])

cv2.fillPoly(mask, [pts], (255), 8, 0)
cv2.imshow('mask', mask)
cv2.waitKey(0)

#[99,40],[139,28],[180,49],[213,87],[245,70],[252,101],[172,145],[89,238],[91,218],[73,108],[82,67]
