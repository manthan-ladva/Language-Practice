import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('Original', img)

rotated_img = cv2.transpose(img)
cv2.imshow('Transpose', rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()