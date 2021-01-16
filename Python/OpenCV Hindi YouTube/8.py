import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

resize= cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow('Resize_image', resize)
cv2.waitKey(0)

img_scaled = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaled', img_scaled)
cv2.waitKey(0)

img_area = cv2.resize(img, (300,300), interpolation=cv2.INTER_AREA)
cv2.imshow('Area', img_area)
cv2.waitKey(0)

cv2.destroyAllWindows()