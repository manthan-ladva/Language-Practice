import cv2
import numpy as np

img = cv2.imread('1.jpg')
height, width = img.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((height/4, width/4),90, 1)
rotation_image = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow('Original', img)
cv2.imshow('Rotation', rotation_image)

cv2.waitKey(0)
cv2.destroyAllWindows()