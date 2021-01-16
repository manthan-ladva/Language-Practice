import cv2
import numpy as np

"""img = cv2.imread("1a1de0aa13c684681d9dd7f6202a05fc.jpg")
cv2.imshow('Original', img)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread('1a1de0aa13c684681d9dd7f6202a05fc.jpg', 0)
print(img.shape)
cv2.imshow('Original', img)
cv2.waitKey(0)

ret, tre = cv2.threshold(img, 150,200, cv2.THRESH_BINARY)
cv2.imshow('Gray',tre)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


"""img = cv2.imread('1a1de0aa13c684681d9dd7f6202a05fc.jpg')
print(img.shape)
cv2.imshow('Original', img)
cv2.waitKey()

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', img_hsv)
cv2.waitKey(0)

cv2.imshow('H', img_hsv[:,:,0])
cv2.waitKey(0)
cv2.imshow('S', img_hsv[:,:,1])
cv2.waitKey(0)
cv2.imshow('V', img_hsv[:,:,2])
cv2.waitKey(0)

cv2.destroyAllWindows()"""


"""img = cv2.imread('1a1de0aa13c684681d9dd7f6202a05fc.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

B,G,R = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype='uint8')

cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)

cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)

cv2.imshow('Blue', cv2.merge([zeros, G, R]))
cv2.waitKey(0)

cv2.destroyAllWindows()"""


"""img = cv2.imread('2.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)
print(img.shape)

height, width= img.shape[:2]
print('Height', height)
print('Width', width)

quater_height, quater_width = height/4, width/4
print('Quater_Height', quater_height)
print('Quater_Width', quater_width)

T = np.float32([[1,0,quater_height],
                [0,1,quater_width]])

print(T)

img_trans = cv2.warpAffine(img, T, (height, width))
cv2.imshow('Trans',img_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()"""