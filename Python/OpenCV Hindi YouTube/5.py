import cv2
import numpy as np

img = cv2.imread("1.jpg")
cv2.imshow("Original", img)
cv2.waitKey(0)

height, width = img.shape[:2]
print(height, width)

quater_height, quater_width = height/4, width/4
print(quater_height, quater_width)

T = np.float32([[1,0, quater_height],
                [0,1, quater_width]])
print(T)

img_translations = cv2.warpAffine(img, T, (width, height))

cv2.imshow('Translation', img_translations)
cv2.waitKey(0)

cv2.destroyAllWindows()