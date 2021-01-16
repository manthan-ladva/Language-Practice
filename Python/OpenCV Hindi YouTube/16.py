import cv2
import numpy as np

square = np.zeros((300,300), np.uint8)

cv2.rectangle(square,(50,50), (250,250), 255, -1)
cv2.imshow('Square', square)
cv2.waitKey(0)
cv2.destroyAllWindows()