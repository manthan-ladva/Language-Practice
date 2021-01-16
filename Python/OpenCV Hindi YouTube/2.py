import cv2

img = cv2.imread("1.jpg", 0)
print(img.shape)
cv2.imshow('Original', img)
cv2.waitKey(0)

ret, bw = cv2.threshold(img, 150,200,cv2.THRESH_BINARY)
cv2.imshow('Binary', bw)
cv2.waitKey(0)

cv2.destroyAllWindows()