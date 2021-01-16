import cv2
import numpy as np

img = cv2.imread('1.jpg', 0)
cv2.imshow('Original', img)
cv2.waitKey(0)

height, width = img.shape
laplasian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('lap', laplasian)
cv2.waitKey(0)

cv2.destroyAllWindows()