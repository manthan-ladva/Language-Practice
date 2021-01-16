import cv2

img = cv2.imread('1.jpg')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV', img_hsv)

cv2.imshow('H', img_hsv[:,:,0])
cv2.imshow('S', img_hsv[:,:,1])
cv2.imshow('V', img_hsv[:,:,2])

cv2.waitKey(0)
cv2.destroyAllWindows()