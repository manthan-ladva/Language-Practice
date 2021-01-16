import cv2

img = cv2.imread("1.jpg") # or just pass here ", 0" so that it directly converts into grayscale
print(img.shape)
cv2.imshow('Original', img)
cv2.waitKey(0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
cv2.imshow("Gray_img", gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()