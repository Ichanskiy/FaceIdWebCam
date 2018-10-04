import cv2
import os
import numpy as np
from PIL import Image

count = 30
dirPath = ""
listFiles = []

for (dirPath, dirnames, filenames) in os.walk("C:/Users/Ichanskiy/PycharmProjects/FaceIdWebCam/FacialRecognition/input/"):
    listFiles = filenames
    print(list)
    print(dirPath)
    print(dirnames)
    break

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for fileName in listFiles:
    im = Image.open(dirPath + fileName)
    face_id = fileName.replace(".jpg", "")
    im2arr = np.array(im)

    img = cv2.flip(im2arr, 1)  # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for i in range(count):
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Save the captured image into the datasets folder
            cv2.imwrite("C:/Users/Ichanskiy/PycharmProjects/FaceIdWebCam/FacialRecognition/dataset/User." + str(
                face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            count += 1
