import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

blur = cv2.blur(img, (9,9))
cv2.imshow('Blur', blur)
cv2.waitKey(0)

gaussian = cv2.GaussianBlur(img, (9,9), 0)
cv2.imshow('Gaussian', gaussian)
cv2.waitKey(0)

cv2.destroyAllWindows()