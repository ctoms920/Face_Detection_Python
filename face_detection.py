import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\Cyril Tom Mathew\Desktop\haarcascade_frontalface_default.xml")
image = cv2.imread("C:\\Users\Cyril Tom Mathew\Desktop\ggg.jpg")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)
print("{0} Faces Detected".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w,y+h), (0,255,0),2)

cv2.imshow("Faces Detected!!", image)
cv2.waitKey(0)
