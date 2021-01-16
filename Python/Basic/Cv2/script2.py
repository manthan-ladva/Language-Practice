import cv2
import glob2

images = glob2.glob("*.jpg")

for i in images:
    img = cv2.imread(i, 0)
    re =  cv2.resize(img, (100, 100))
    cv2.imshow('Heyyy', re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + i, re)
