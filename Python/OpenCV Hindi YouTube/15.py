import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

M = np.ones(img.shape, dtype='uint8') * 150
added = cv2.add(img, M)
cv2.imshow('Add', added)
cv2.waitKey(0)

Mul = cv2.multiply(img, M)
cv2.imshow('Mul', Mul)
cv2.waitKey(0)

Sub = cv2.subtract(img, M)
cv2.imshow('Subt', Sub)
cv2.waitKey(0)

cv2.destroyAllWindows()