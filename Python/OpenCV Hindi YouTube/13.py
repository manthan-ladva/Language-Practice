import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

smaller = cv2.pyrUp(img)
larger = cv2.pyrDown(img)

cv2.imshow('Smaller', smaller)
cv2.imshow('Larger', larger)
cv2.waitKey(0)

cv2.destroyAllWindows()