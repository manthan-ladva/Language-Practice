import cv2
import numpy as np

img = cv2.imread('2.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

height, width = img.shape[:2]



cv2.destroyAllWindows()