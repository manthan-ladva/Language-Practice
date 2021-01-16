import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

height, width = img.shape[:2]

start_row, start_col = int(height*.20), int(width*.20)
end_row, end_col = int(height*.50), int(width*.50)

cropped = img[start_row:end_row, start_col:end_col]
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()