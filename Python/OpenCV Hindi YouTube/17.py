import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

kernel_3x3 = np.ones((3,3), np.float32)/9
blured = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('blured3x3', blured)
cv2.waitKey(0)

kernel_9x9 = np.ones((9,9), np.float32)/81
blured1 = cv2.filter2D(img, -1, kernel_9x9)
cv2.imshow('blured9x9', blured1)
cv2.waitKey(0)

cv2.destroyAllWindows()