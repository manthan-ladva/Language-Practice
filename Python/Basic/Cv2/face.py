import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


img = cv2.imread("photo.jpg")


faces = face_cascade.detectMultiScale(img,
scaleFactor = 1.2,
minNeighbors = 5)


for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w,y+h), (255, 0, 0), 3)

print(type(faces))
print(faces)
print(img.shape)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow('Gray', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
